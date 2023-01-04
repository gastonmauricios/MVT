from django.shortcuts import render

from .models import Curso, Profesor, Estudiante
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, authenticate



from AppCoder.forms import CursoForm, ProfeForm, RegistroUsuarioForm, UserEditForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DetailView, DeleteView

from django.contrib.auth.decorators import login_required #para vistas basaas en funciones def
from django.contrib.auth.mixins import LoginRequiredMixin # finciones basadas en clases este no se usa si no estas logueado

# Create your views here
@login_required
def curso(request): #las views reciben request
    cursito= Curso(nombre= "Python", comision=123456)
    cursito.save()
    cadena_texto=f"curso guardado: {cursito.nombre}, comision: {cursito.comision} "
    return HttpResponse(cadena_texto)

@login_required
def cursos(request): #las views reciben request
    return render(request, "AppCoder/cursos.html")

@login_required
def estudiantes(request): #las views reciben request
    return render(request, "AppCoder/estudiantes.html")

@login_required
def profesores(request): #las views reciben request
    return render(request, "AppCoder/profesores.html")

@login_required
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
@login_required
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
@login_required       
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
            profesores=Profesor.objects.all()
            return render(request, 'AppCoder/Profesores.html' ,{'profesores': profesores, 'mensaje': 'ok el Profe se guardo correctamente'})

        else:
            return render(request, 'AppCoder/ProfeFormulario.html',{'form': form, 'mensaje': 'info NO valida'})
    else:
        formulario=ProfeForm
        return render(request, 'AppCoder/ProfeFormulario.html',{'form': formulario})
@login_required
def busquedaComision(request):
    return render(request, 'AppCoder/busquedaComision.html')
@login_required
def buscar(request):
    
    comision= request.GET['comision']
    if comision!="":
        cursos=Curso.objects.filter(comision__icontains=comision)
        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos': cursos})
    
    else:
        return render(request, 'AppCoder/busquedaComision.html', {'mensaje': 'che ingresa una comision para buscar!'})
@login_required
def leerProfesores(request):

    profesores=Profesor.objects.all() # lista de todos los profesores
    return render(request, 'AppCoder/Profesores.html', {'profesores': profesores})
@login_required
def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    print(profesor)
    profesor.delete()
    profesores=Profesor.objects.all()
    return render (request, 'AppCoder/Profesores.html', {'profesores': profesores, 'mensaje': 'profesor eliminado correctamente' })
@login_required
def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method=='POST':
        form=ProfeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profesor.nombre=info['nombre']
            profesor.apellido=info['apellido']
            profesor.email=info['email']
            profesor.profesion=info['profesion'] #piso los datos con nuevos datos
            profesor.save()
            profesores=Profesor.objects.all()
            return render (request, 'AppCoder/Profesores.html', {'profesores': profesores, 'mensaje': 'profesor editado correctamente' })
        pass
    else:
        formulario= ProfeForm(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})
        return render(request, 'AppCoder/editarProfesor.html', {'form': formulario, 'profesor': profesor})

# VISTAS BASADAS EN CLASES

class EstudianteList(LoginRequiredMixin, ListView):
    model= Estudiante
    template_name= 'AppCoder/estudiantes.html'

class EstudianteCreacion(LoginRequiredMixin, CreateView):
    model= Estudiante
    success_url= reverse_lazy('estudiante_list') # re-direcciona es de django
    fields=['nombre', 'apellido','email']


class EstudianteUpdate(LoginRequiredMixin, UpdateView): #  vista usada para editar
    model= Estudiante
    success_url= reverse_lazy('estudiante_list') # re-direcciona es de django
    fields=['nombre', 'apellido','email']




class EstudianteDetalle(LoginRequiredMixin, DetailView): # vista usada para mostrar datos
    model=Estudiante
    template_name= 'AppCoder/estudiante_detalle.html'

class EstudianteDelete(LoginRequiredMixin, DeleteView): # vista usada para eleiminar
    model=Estudiante
    success_url= reverse_lazy('estudiante_list')

#vista de registro usuario!!!!


def register(request):
    if request.method=='POST':
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save() #guardo en la base de dato el objeto que trae formulario
            
            return render(request, 'AppCoder/inicio.html',  { 'mensaje': f'usuario {username} creado correctamente' })
        else:
             return render(request, 'AppCoder/register.html',  {'form': form, 'mensaje': ' error al crear usuario' })

    


    else:
        form=RegistroUsuarioForm()
        return render(request, 'AppCoder/register.html', {'form': form})


def login_request(request):
    if request.method=='POST':
        pass
    else:
        form=AuthenticationForm()
        return render(request, 'AppCoder/login.html', {'form': form})

def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info['username']
            clave=info['password']
            usuario=authenticate(username=usu, password=clave) #verifica si el e usuario existe
            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppCoder/inicio.html',{'mensaje':f'Usuario  {usu} logueado correcatamente'} )
            else:
                return render(request, 'AppCoder/login.html',{'form': form ,'mensaje': 'Usuario o contraseña  incorrecata'} )
        else:
            return render(request, 'AppCoder/login.html',{'form': form, 'mensaje': 'Usuario o contraseña  incorrecata'} )
    else:
        form= AuthenticationForm()
        return render(request, 'AppCoder/login.html', {'form': form })

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=='POST':
        pass
    else:
        form=UserEditForm(isinstance=usuario)
        return render(request, 'AppCoder/editarPerfil.html', {'form': form, 'nombreusuario': usuario.username})


     


