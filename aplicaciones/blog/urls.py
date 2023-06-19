from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'home'),
    
    path('crearAutor/',crearAutor, name = 'crear_autor'),
    path('listarAutor/',listarAutor, name = 'listar_autor'),
    path('editarAutor/<int:id>',editarAutor, name = 'editar_autor'),
    path('eliminarAutor/<int:id>',eliminarAutor, name = 'eliminar_autor'),

    path('administrador/',administrador, name = 'administrador'),
    path('generales/',generales, name = 'generales'),
    path('aplicacion/',aplicacion, name = 'aplicacion'),
    path('tutoriales/',tutoriales, name = 'tutoriales'),
   
    path('<slug:slug>/',detallePost, name = 'detalle_post'),

    

]