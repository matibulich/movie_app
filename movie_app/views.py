from django.shortcuts import render

from movie_app.models import Pelicula
from movie_app.forms import Carga_peliculas,  Usuario_registro, Usuario_edicion
from django.contrib.auth.forms import AuthenticationForm,  UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages




def inicio(request):
      return render(request, "movie_app/inicio.html")

@login_required
def portal(request):

      return render(request, "movie_app/portal.html")



#FORMULARIO PELICULAS
def peliculas(request):

      if request.method == 'POST':

            miFormulario = Carga_peliculas(request.POST, files=request.FILES) 



            if miFormulario.is_valid():   

                  informacion = miFormulario.cleaned_data

                  pelicula = Pelicula (nombre=informacion['nombre'], genero=informacion['genero'], plataforma=informacion['plataforma'], puntuacion=informacion['puntuacion'], comentarios=informacion['comentarios'], portada=informacion['portada']) 
                  pelicula.usuario = request.user
                  pelicula.save()
                  messages.success(request, "Pelicula Cargada Correctamente")

                  return render(request, "movie_app/portal.html") 

      else: 

            miFormulario= Carga_peliculas() 
      return render(request, "movie_app/peliculas.html", {"miFormulario":miFormulario})

#FORMULARIO EDITAR PELICULAS

def editar_pelicula(request, pelicula_nombre):

      
      pelicula = Pelicula.objects.get(nombre=pelicula_nombre)

      
      if request.method == 'POST':

            miFormulario = Carga_peliculas(request.POST,  files=request.FILES) 

     
            if miFormulario.is_valid():   
                  informacion = miFormulario.cleaned_data

                  pelicula.nombre = informacion['nombre']
                  pelicula.genero = informacion['genero']
                  pelicula.plataforma = informacion['plataforma']
                  pelicula.puntuacion = informacion['puntuacion']
                  pelicula.comentarios = informacion['comentarios']
                  pelicula.portada = informacion['portada']

                  pelicula.save()
                  messages.success(request, "Pelicula Editada Correctamente")
                  return render(request, "movie_app/mostrar_peliculas.html") 
     
      else: 
            
            miFormulario= Carga_peliculas(initial={'nombre': pelicula.nombre, 'genero':pelicula.genero, 
            'plataforma':pelicula.plataforma, 'puntuacion':pelicula.puntuacion, 'comentarios':pelicula.comentarios, 'portada':pelicula.portada }) 

      
      return render(request, "movie_app/editar_pelicula.html", {"miFormulario":miFormulario, "editar_pelicula":pelicula_nombre})




 #FORMULARIO LOGIN
 

def login_request(request):
      if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST) 
            if form.is_valid():

                  usuario = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')

                  

                  user = authenticate(username = usuario , password = password)

         

                  if user is not None:
                        login(request, user)

                        return render (request, "movie_app/portal.html", )
                  else:
                  
                        return render (request, "movie_app/inicio.html", {"mensaje":"Error en los datos"})
            else:
                        return render(request, "movie_app/inicio.html", messages.error(request, "Contraseña incorrecta"))
      
      form = AuthenticationForm()
      return render(request, "movie_app/login.html", {'form': form} )

 #FORMULARIO REGISTRO
def registro(request):
      
      if request.method == "POST":

            form = Usuario_registro(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()
                  messages.success(request, "Usuario creado Correctamente")

                  return render(request, "movie_app/inicio.html")

      else: 
            form = Usuario_registro()

      return render(request, "movie_app/registro.html", {"form": form})

  

# FORMULARIO EDITAR USUARIO 
def editar_usuario(request):
      
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = Usuario_edicion(request.POST)
            if miFormulario.is_valid(): 
                  informacion = miFormulario.cleaned_data
                  
                 
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.last_name = informacion['last_name']
                  usuario.first_name = informacion['first_name']

                  usuario.save()
                  messages.success(request, "Usuario editado Correctamente")
                  return render(request, "movie_app/portal.html") 

      else:
            
            miFormulario = Usuario_edicion(initial={'email':usuario.email})
      
 
      return render(request, "movie_app/editar_usuario.html", {"miFormulario": miFormulario, "usuario": usuario})


# FORMULARIO MOSTRAR PELICULAS
class Mostrar_pelicula(ListView):
      model = Pelicula
      template_name = "movie_app/mostrar_peliculas.html"


 #BORRAR / EDITAR / VER


# class Pelicula_editar(UpdateView):

#       model = Pelicula
#       success_url = "/movie_app/peliculas/list"
#       fields  = ['nombre', 'genero','plataforma','puntuacion','comentarios','portada']


class Pelicula_detalle(DetailView):

      model = Pelicula
      template_name = "movie_app/pelicula_detalle.html"

class Borrar_pelicula(DeleteView):

      model = Pelicula
      success_url = "/movie_app/peliculas/list"


