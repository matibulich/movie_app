from django.urls import path

from movie_app import views

from django.contrib.auth.views import LogoutView






urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('portal', views.portal, name='portal'),
    path('peliculas', views.peliculas, name='peliculas'),
    path('login', views.login_request, name='login'),
    path('registro', views.registro, name='registro'),
    path('logout',LogoutView.as_view(template_name='movie_app/logout.html'), name='logout'),
    path('editar_usuario', views.editar_usuario, name='editar_usuario'),
    path('peliculas/list', views.Mostrar_pelicula.as_view(), name='listar_pelicula'),
    path(r'^borrar/(?P<pk>\d+)$', views.Borrar_pelicula.as_view(), name='borrar_pelicula'),
    path(r'^(?P<pk>\d+)$', views.Pelicula_detalle.as_view(), name='Detail'),
    path('peliculas/<pelicula_nombre>/', views.editar_pelicula, name="editar_pelicula"),
 
   

    
]

