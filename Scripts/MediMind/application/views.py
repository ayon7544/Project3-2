from django.shortcuts import render
from django.http import JsonResponse
from .forms import *


def homepage(request):
    return render(request, 'homepage.html')
def login(request):
    return render(request, 'loginpage.html')

def diseaseform(request):
    return render(request, 'diseaseform.html')
def disease_form_view(request):
    return render(request, 'disease_form.html')
def get_disease_options(request):
    diseases = Disease.objects.all()
    options = [{'id': disease.id, 'name': disease.name} for disease in diseases]
    return JsonResponse({'options': options})

def submit_form(request):
    if request.method == 'POST':
        # Process the form data (not shown in this example)
        return JsonResponse({'success': True, 'next_page': '/next-page/'})
    return JsonResponse({'success': False})


