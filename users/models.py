from django.db import models

# Create your models here.

class users(models.Model): #trayendo el modelo
    username = models.CharField(blank=False, max_length=100)
    number = models.IntegerField()

