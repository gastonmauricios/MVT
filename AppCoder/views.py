from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here

def curso(request): #las views reciben request
    cursito= Curso(nombre= "Python", comision=123456)
    cursito.save()
    cadena_texto=f"curso guardado: {cursito.nombre}, comision: {cursito.comision} "
    return HttpResponse(cadena_texto)


def cursos(request): #las views reciben request
    return render(request, "AppCoder/cursos.html")


def estudiantes(request): #las views reciben request
    return render(request, "AppCoder/estudiantes.html")


def profesores(request): #las views reciben request
    return render(request, "AppCoder/profesores.html")


def entregables(request): #las views reciben request
    return render(request, "AppCoder/entregables.html")

def inicio(request): #las views reciben request
    return render(request, "AppCoder/inicio.html")