from django.urls import path
from . import views

urlpatterns = [
    path('', views. homepage, name='homepage'),
    path('diseaseform/', views.diseaseform, name='diseaseform'),
    path('predictedDisease/<str:disease>/', views.predictedDisease,name='predictedDisease'),
    path('appointmentform/', views.appointmentform, name='appointmentform'),
    path('payment/', views.payment, name='payment'),
    path('resource/', views.resource, name='resource'),
    path('seminar/', views.seminar, name='seminar'),

    path('findmedicine/', views.findmedicine, name="findmedicine"),
    path('bookings/', views.bookings, name="bookings"),
    path('Thankyou/', views.Thankyou, name="Thankyou"),
]
