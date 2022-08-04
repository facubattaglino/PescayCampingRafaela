from cProfile import label
from django.db import models
from re import M
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class cañas(models.Model):
    marca = models.CharField(label = "Marca: " ,max_length= 50)
    tramos = models.IntegerField(label = "Tramos: ")
    libras = models.IntegerField(label = "Libras")

class reeles(models.Model):
    marca = models.CharField(label = "Marca: ",max_length= 50)
    tipo = models.CharField(label = "Tipo de reel:",max_length= 50)

class accesorios(models.Model):
    pass

class armeria(models.Model):
    pass

class indumentaria(models.Model):
    pass