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
