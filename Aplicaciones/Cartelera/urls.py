#configurando redireccionamiento 
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('listadoGeneros/', views.ListadoGeneros, name='listado_generos'),
    path('eliminarGenero/<id>',views.eliminarGenero, name='eliminarGenero'),
    path('editarGenero/<id>', views.editarGenero,name='editarGenero'),
    path('guardarGenero/',views.guardarGenero, name='guardarGenero'),
    path('procesoActualizarGenero/', views.procesoActualizarGenero,name='procesoActualizarGenero'),
    path('listadoDeDirectores/',views.ListadoDirectores , name='listado_directores'),
    path('listadoDePeliculas/',views.ListadoPeliculas, name='listado_Peliculas'),
    path('listadoDePaises/',views.ListadoPaises, name='listado_Paises'),
    
    path('nuevoGenero/',views.nuevoGenero, name='nuevoGenero'),
    path('nuevoDirector/',views.nuevoGenero, name='nuevoDirector'),

    path('procesoActualizarPais/', views.procesoActualizarPais,name='procesoActualizarPais'),
    path('gestionCines/', views.gestionCines,name='gestionCines'),
    path('guardarCine/', views.guardarCine, name='guardarCine'),
    
    path('cines/', views.vista_cines, name='vista_cines'),
    path('vista_cines/', views.vista_cines, name='vista_cines'),
    
]
