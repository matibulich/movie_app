from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Carga_peliculas(forms.Form):

    plataforma_opc =(
        ("Netflix","Netflix"),
        ("Amazon","Amazon"), 
        ("Hbo","HBO"), 
        ("Disney","Disney"),
        ("Apple","Apple"), 
        ("Cine","Cine"), 
         
    )


    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    plataforma = forms.ChoiceField(choices=plataforma_opc)
    puntuacion = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'range', 'step':'0', 'min':'1', 'max':'10'}))
    comentarios= forms.CharField(widget=forms.Textarea)
    portada = forms.ImageField() 
    # usuario = forms.CharField(max_length=30)




class Usuario_registro(UserCreationForm):
    
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite la contraseña', widget=forms.PasswordInput)
    email = forms.EmailField()
    last_name: forms.CharField()
    first_name: forms.CharField()

    class Meta:
        model = User                                               
        fields = ['username',  'password1', 'password2','email', 'last_name', 'first_name']
        labels = {'username': 'Usuario', 'email':'Correo','last_name': 'Apellido', 'first_name':'Nombre'}
        help_texts= {k:"" for k in fields}

class Usuario_edicion(UserCreationForm): 
    

    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite la contraseña', widget=forms.PasswordInput)
    email = forms.EmailField()
    last_name: forms.CharField()
    first_name: forms.CharField()

    class Meta:
        model = User                                               
        fields = [ 'password1', 'password2','email', 'last_name', 'first_name']
        labels = { 'email':'Correo','last_name': 'Apellido', 'first_name':'Nombre'}
        help_texts= {k:"" for k in fields}