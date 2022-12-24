from django.shortcuts import render
from .models import Curso, Profesor
from django.http import HttpResponse

from AppCoder.forms import CursoForm, ProfeForm
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

""" def cursoFormulario(request):     # formulario
    if request.method=='POST':
        nombre= request.POST['nombre']
        comision= request.POST['comision']
        print(nombre, comision)
        curso= Curso (nombre=nombre, comision=comision)
        curso.save()
        return render (request, 'AppCoder/inicio.html', {'mensaje': 'Curso guardado exitosamente'})
        
    else:
        return render (request, 'AppCoder/cursoFormulario.html') """

def cursoFormulario(request):
    if request.method=='POST':
        form= CursoForm(request.POST)
        print('---------------------------')
        print(form)
        print('---------------------------')
        if form.is_valid():
            informacion=form.cleaned_data #convierte la info en modo formulario a un diccionario
            print(informacion)
            nombre= informacion['nombre']
            comision= informacion['comision']
            curso= Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, 'AppCoder/inicio.html',{'mensaje': 'ok el Curso se guardo correctamente'})
        else:
            return render(request, 'AppCoder/cursoFormulario.html',{'form': form, 'mensaje': 'info NO valida'})

        
    else:
        formulario= CursoForm()
        return render (request, 'AppCoder/cursoFormulario.html', {'form': formulario})
        
def profeFormulario(request):
    if request.method=='POST':
        form= ProfeForm(request.POST)
        
                
        if form.is_valid():
            informacion=form.cleaned_data #convierte la info en modo formulario a un diccionario
            nombre= informacion ['nombre']
            apellido= informacion ['apellido']
            email= informacion ['email']
            profesion=informacion ['profesion']
            profe=Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render(request, 'AppCoder/inicio.html',{'mensaje': 'ok el Profe se guardo correctamente'})

        else:
            return render(request, 'AppCoder/ProfeFormulario.html',{'form': form, 'mensaje': 'info NO valida'})
    else:
        formulario=ProfeForm
        return render(request, 'AppCoder/ProfeFormulario.html',{'form': formulario})

def busquedaComision(request):
    return render(request, 'AppCoder/busquedaComision.html')

def buscar(request):
    comision= request.GET('comision')
    
    if comision!="":
        cursos= Curso.objects.filter(comision=comision)
        return render(request, 'AppCoder/resultadoBusqueda.html', {'cursos': cursos})
    else:
        return render(request, 'AppCoder/busquedaComision.html', {'mensaje': 'ingrese comision'})

