from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class CursoForm(forms.Form):
    nombre= forms.CharField(label='Nombre Curso', max_length=50)
    comision= forms.IntegerField(label='Comision')

class ProfeForm(forms.Form):
    nombre= forms.CharField(label='Nombre Profesor', max_length=50)
    apellido= forms.CharField(label='Apellido Profesor', max_length=50)
    email= forms.EmailField(label='Email Profesor')
    profesion= forms.CharField(label='Profesion Profesor', max_length=50)

class RegistroUsuarioForm(UserCreationForm):
    
    email=forms.EmailField(label='email profesor')
    password1= forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields} # borra campos y sean vacios, borra textos de ayuda por defecto.
    




