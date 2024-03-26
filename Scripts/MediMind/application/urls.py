from django.urls import path
from . import views

urlpatterns = [
    path('', views. homepage, name='homepage'),
    path('login/',views.login,name='login'),
    path('diseaseform/', views.diseaseform, name='diseaseform'),
    path('get-disease-options/', views.get_disease_options, name='get_disease_options'),
    path('submit-form/', views.submit_form, name='submit_form'),
]