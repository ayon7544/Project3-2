import threading
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# #** For some reason this is not working for me!!
# from validate_email import validate_email
# #** This email_validator is to resolve previous validator.
from email_validator import validate_email
# #** You can use any one from these two validator

from .models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from helpers.decorators import auth_user_should_not_access
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = "Activate your account"
    email_body = render_to_string("authentication/activate.html", {
        "user": user,
        "domain": current_site,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": generate_token.make_token(user)
    })
    email = EmailMessage(subject=email_subject,
                         body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email])
    EmailThread(email).start()


@auth_user_should_not_access
def register(request):
    if request.method == 'POST':
        context = {'has_error': False, "data": request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if not username:
            messages.add_message(request, messages. ERROR,
                                 "Username is required!")
            context['has_error'] = True
        elif User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR,
                                 "Username is already taken!")
            context['has_error'] = True
        if not email:
            messages.add_message(request, messages. ERROR,
                                 "Email address is required!")
            context['has_error'] = True
        elif not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 "Enter a valid email address!")
            context['has_error'] = True
        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 "An account already exists with that email!")
            context['has_error'] = True
        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 "Password must be at least 6 characters.")
            context['has_error'] = True
        elif password != password2:
            messages.add_message(request, messages.ERROR,
                                 "Password mismatch!")
            context['has_error'] = True
        if context['has_error']:
            # messages.add_message(request, messages.WARNING,
            #                      "Please provide a valid information!")
            return render(request, "authentication/loginpage.html", context)
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        send_activation_email(user, request)
        messages.add_message(request, messages.SUCCESS,
                             "We sent you an email to verify your account.")
        return redirect("login")
    return render(request, "authentication/loginpage.html")


@auth_user_should_not_access
def resend_authentication(request):
    if request.method == 'POST':
        context = {'has_error': False, "data": request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        if not username:
            messages.add_message(request, messages. ERROR,
                                 "Username is required!")
            context['has_error'] = True
        if not email:
            messages.add_message(request, messages. ERROR,
                                 "Email address is required!")
            context['has_error'] = True
        elif not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 "Enter a valid email address!")
            context['has_error'] = True
        if context['has_error']:
            messages.add_message(request, messages.WARNING,
                                 "Please provide a valid information!")
            return render(request, "authentication/resend-authentication.html",
                          context)
        try:
            user = User.objects.get(username=username)
            if not user.email == email:
                messages.add_message(request, messages.ERROR,
                                     "Wrong username or email!")
                return render(request,
                              "authentication/resend-authentication.html",
                              context)
        except User.DoesNotExist:
            user = None
        if user is None:
            try:
                user = User.objects.get(email=email)
                if not user.username == username:
                    messages.add_message(request, messages.ERROR,
                                         "Wrong username or email!")
                    return render(request,
                                  "authentication/resend-authentication.html",
                                  context)
            except User.DoesNotExist:
                user = None
        if user is None:
            messages.add_message(request, messages.ERROR,
                                 "Wrong username or email!")
            return render(request, "authentication/resend-authentication.html",
                          context)
        # user = User.objects.get(username=username, email=email)
        if user.is_email_verified:
            messages.add_message(request, messages.INFO,
                                 "Email is already verified! Try to login.")
            return render(request, "authentication/loginpage.html")
        send_activation_email(user, request)
        messages.add_message(request, messages.SUCCESS,
                             "We sent you an email to verify your account.")
        return redirect("login")
    return render(request, "authentication/resend-authentication.html")


@auth_user_should_not_access
def login_user(request):
    if request.method == "POST":
        context = {"data": request.POST}
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if not user.is_email_verified:
                messages.add_message(request, messages.WARNING,
                                     "User is not authenticated!")
                # messages.add_message(request, messages.INFO,
                # "Fill the form to confirm mail verification.")
                return render(request,
                              "authentication/resend-authentication.html")
            login(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 f"Welcome {user.username}")
            return redirect(reverse("login"))
        else:
            messages.add_message(request, messages.ERROR,
                                 "Invalid username or password")
            return render(request, "authentication/loginpage.html", context)
    return render(request, "authentication/loginpage.html")


def logout_user(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,
                         "Successfully logged out")
    return redirect(reverse("login"))


def activate_user(request, uidb64, token):
    try:
        # uid = force_text(urlsafe_base64_decode(uidb64))
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    # except Exception as e:
    except User.DoesNotExist:
        user = None
    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.add_message(request, messages.SUCCESS,
                             "Email verified successfully, you can now login")
        return redirect(reverse("login"))
    return render(request, "authentication/activate-failed.html",
                  {"user": user})


def delete_users(request):
    if request.method == "POST":
        # context = {"data": request.POST}
        username = request.POST.get("username")
        if username == "All":
            count, _ = User.objects.all().delete()
            messages.add_message(request, messages.SUCCESS,
                                 f"All {count} users have been successfully deleted.")
        else:
            users = User.objects.filter(username=username)
            count = users.delete()[0]
            if count > 0:
                messages.add_message(request, messages.SUCCESS,
                                     f"Username '{username}' have been successfully removed")
            else:
                messages.add_message(request, messages.ERROR,
                                     f'No user found with username "{username}"')
        return redirect(reverse("delete_users"))
    return render(request, "_partials/delete-user.html")
