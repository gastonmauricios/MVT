from django.db import models


# Create your models here. # ESTOS SON LOS MODELOS DE TABLAS DE BASE DE DATOS, los objetos se crean en un views
class Curso(models.Model): # es una herencia objeto Clase curso tiene un models, campos para llenar cosas.
  
    nombre=models.CharField(max_length=50) # campo de texto , creo objetos!!
    comision=models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {str(self.comision)}'

class Estudiante(models.Model): # es una herencia objeto
    
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
   
class Profesor(models.Model): # es una herencia objeto
    
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)
       
class Entregable(models.Model): # es una herencia objeto
    
    nombre=models.CharField(max_length=50) # campo de texto
    fecha_de_entrega=models.DateField()
    entregado=models.BooleanField() # si o no true o false






  