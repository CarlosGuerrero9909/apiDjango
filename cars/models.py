from django.db import models

# Create your models here.

class cars(models.Model):
    fabricante = models.CharField(blank=False, max_length=50)
    marca = models.CharField(blank=False, max_length=50)
    cilindraje = models.FloatField()
    

