from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here
def curso(request): #las views reciben request
    cursito= Curso(nombre= "Python", comision=34645)
    cursito.save()
    cadena_texto=f"curso guardado: {cursito.nombre}, comision: {cursito.comision} "
    return HttpResponse(cadena_texto)