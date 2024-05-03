from django.db import models


class Symptom(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
    
class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    avoid_foods_and_drinks = models.TextField()
    examination_preparation = models.TextField()

    def __str__(self):
        return self.name
    
class Medicine(models.Model):
    medicine = models.CharField(max_length=30)
    quantity = models.DecimalField(decimal_places=0, max_digits=3)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.medicine


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    medicine_r= models.CharField(max_length=30)
    quantity_r = models.DecimalField(decimal_places=0, max_digits=3)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(choices=TICKET_STATUSES,
                              default=BOOKED, max_length=2)

    def __str__(self):
        return self.email
    

class Appointment(models.Model):
    doctor_name = models.CharField(max_length=100)
    appointment_mood = models.CharField(max_length=100)
    appointment_time = models.DateTimeField()
    appointment_length = models.IntegerField()

    def __str__(self):
        return f"{self.doctor_name} - {self.appointment_time}"


