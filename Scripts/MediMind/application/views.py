from django.shortcuts import render,redirect
from . import DiseaseClassifier
from .models import Symptom

def homepage(request):
    return render(request, 'homepage.html')
def login(request):
    return render(request, 'loginpage.html')

def diseaseform(request):
    if request.method == 'POST':
        Disease1 = request.POST.get('disease1')
        Disease2 = request.POST.get('disease2')
        Disease3 = request.POST.get('disease3')
        Disease4 = request.POST.get('disease4')
        Disease5 = request.POST.get('disease5')
        loaded_model = DiseaseClassifier.DiseaseClassifier.load_model("disease_model.sav")
        symptom = [Disease1,Disease2,Disease3,Disease4,Disease5]
        input_test = loaded_model.symptoms(symptom)
        predicted = loaded_model.gnb.predict(input_test)
        disease = loaded_model.get_disease(predicted)
        return redirect('predictedDisease',disease)
    symptoms = Symptom.objects.all()
    return render(request, 'diseaseform.html', {'symptoms': symptoms})

def predictedDisease(request,disease):
    return render(request,'predictedDisease.html',{'disease':disease})


