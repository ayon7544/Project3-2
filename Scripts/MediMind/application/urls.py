from django.urls import path
from . import views

urlpatterns = [
    path('', views. homepage, name='homepage'),
    path('login/',views.login,name='login'),
    path('diseaseform/', views.diseaseform, name='diseaseform'),
    path('predictedDisease/<str:disease>/', views.predictedDisease, name='predictedDisease'),
]