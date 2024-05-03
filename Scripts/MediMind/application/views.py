from django.shortcuts import render, redirect
from . import DiseaseClassifier
from .models import Symptom
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def homepage(request):
    return render(request, 'medi_mind/homepage.html')


@login_required
def diseaseform(request):
    if request.method == 'POST':
        Disease1 = request.POST.get('disease1')
        loaded_model = DiseaseClassifier.DiseaseClassifier.load_model(
            "disease_model.sav")
        symptom = [Disease1]
        input_test = loaded_model.symptoms(symptom)
        predicted = loaded_model.gnb.predict(input_test)
        disease = loaded_model.get_disease(predicted)
        return redirect('predictedDisease', disease)
    symptoms = Symptom.objects.all()
    return render(request, 'application/diseaseform.html',
                  {'symptoms': symptoms})


@login_required
def predictedDisease(request, disease):
    details = Disease.objects.get(name=disease)
    return render(request, 'application/predictedDisease.html',
                  {'disease': disease,'description':details.description,'avoid':details.avoid_foods_and_drinks,'examination_preparation':details.examination_preparation})

@login_required  
def appointmentform(request):
    if request.method == "POST":
        return redirect(Thankyou)
    Appointments=Appointment.objects.all()
    return render(request, 'medi_mind/Appointmentform.html',{'Appointments':Appointments})

def payment(request):
    return render(request, 'medi_mind/payment.html')

@login_required  
def resource(request):
    return render(request, 'medi_mind/resource.html')

@login_required  
def seminar(request):
    return render(request, 'medi_mind/seminar.html')

def homemedicine(request):
        return render(request, 'pharmacy/pharmacyhome.html')
    
@login_required  
def findmedicine(request):
    context = {}
    if request.method == 'POST':
        medicine_r = request.POST.get('medicine')
        medicine_list = Medicine.objects.filter(
                medicine=medicine_r)
        if medicine_list:
            return render(request, 'pharmacy/list.html', locals())
        else:
            context["error"] = "Sorry this one is not available"
            return render(request, 'pharmacy/findmedicine.html', context)
    else:
        return render(request, 'pharmacy/findmedicine.html')



def bookings(request):
        return render(request, 'pharmacy/bookings.html')
def payment(request):
    return render(request, 'pharmacy/payment.html')
def Thankyou(request):
    return render(request, 'pharmacy/Thankyou.html')


