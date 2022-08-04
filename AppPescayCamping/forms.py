from dataclasses import fields
from random import choices
from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from .models import *

#Formulario para Cañas
class NuevaCaña(forms.Form):
    nombre = forms.CharField(max_length=60, label = "Nombre Caña")
    tramo = forms.IntegerField(label = "Tramos")
    libras = forms.CharField(label = "Libras")