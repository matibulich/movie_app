from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pelicula(models.Model):
    nombre= models.CharField(max_length=30, null=True)
    genero= models.CharField(max_length=30)
    plataforma= models.CharField(max_length=30)
    puntuacion=models.IntegerField()
    comentarios=models.CharField(max_length=300)
    portada=models.ImageField(upload_to='imagenes_portada', null=True, blank=True) 
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True )
    def __str__(self):
        return f"{self.nombre}"

