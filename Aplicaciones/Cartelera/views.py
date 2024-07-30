from django.shortcuts import redirect, render
from . models import Genero
from . models import Director
from . models import Pelicula
from . models import Pais
from . models import Cine
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request,"home.html")  


def ListadoGeneros(request):
    #Importacion de la base 
    generosBdd=Genero.objects.all()
    
    return render(request,"listadoGeneros.html",{'generos':generosBdd})

#Se recibe el id para eliminar un genero

def eliminarGenero(request,id):
    generoEliminar =Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request,"Genero eliminado Exitosamente.")
    return redirect('listado_generos')

#Renderizando formulario de nuevo genero

def nuevoGenero(request):
    return render(request,'nuevoGenero.html')

def nuevoDIrector(request):
    return render(request,'nuevoDirector.html')


#Insertadno generos en la base de datos 
def guardarGenero(request):
    nom=request.POST['nombre']
    desc=request.POST['descripcion']
    fot=request.FILES.get('foto')
    nuevoGenero=Genero.objects.create(nombre=nom,descripcion=desc,foto=fot)
    messages.success(request,"Genero registrado exitosamente.")
    return redirect('listado_generos')



def ListadoDirectores(request):
    #Importacion de la base
    direcctoresBdd =Director.objects.all()

    return render(request,"listadoDeDIrectores.html",{'director':direcctoresBdd})

def ListadoPeliculas(request):

    peliculasBdd = Pelicula.objects.all()
    return render(request,"listadoDePeliculas.html",{'peliculas':peliculasBdd})


def ListadoPaises(request):

    paisesBdd = Pais.objects.all()
    return render(request,"listadoDePaises.html",{'pais':paisesBdd})


#Renderizando formulario de actualizacion 
def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render(request,'editarGenero.html',{generoEditar:generoEditar})


#Renderizar formularios de actualizar
def editarGenero(request, id):
    generoEdit = Genero.objects.get(id = id)
    return render(request, 'editarGenero.html',{'generoEditar': generoEdit})
#Actualizando los nuevos datos en la BDD

def procesoActualizarGenero(request):
    id=request.POST['id']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    generoConsultado = Genero.objects.get(id=id)
    generoConsultado.nombre = nombre
    generoConsultado.descripcion = descripcion
    generoConsultado.save()
    messages.success(request,"Genero actualizado correctamente")
    return redirect('listado_generos')


def procesoActualizarPais(request):
    id=request.POST['id']
    nombre = request.POST['nombre']
    descripcion = request.POST['continente']
    PaisConsultado = Genero.objects.get(id=id)
    PaisConsultado.nombre = nombre
    PaisConsultado.descripcion = descripcion
    PaisConsultado.save()
    messages.success(request,"Pais actualizado correctamente")
    return redirect('listadoDePaises')




#FUNCION PARA GESTIONAR EL CRUD DE cINER 

def gestionCines(request):
    cines = Cine.objects.all()  # Cambia el nombre de la variable para ser más descriptivo
    return render(request, 'gestionCines.html', {'cine': cines}) 

#Insertando cines mediante AJAX en la Base de Datos


#Cines
#Cines
def gestionCines(request):
    cines = Cine.objects.all()  # Asegúrate de que 'Cine' es tu modelo
    return render(request, 'gestionCines.html', {'cine': cines})
#Insertando cines mediante AJAX en la Base de Datos
def guardarCine(request):
    if request.method == 'POST':
        nom = request.POST.get("nombre")
        dir = request.POST.get("direccion")
        tel = request.POST.get("telefono")
        nuevoCine = Cine.objects.create(nombre=nom, direccion=dir, telefono=tel)
        return JsonResponse({
            'estado': True,
            'mensaje': 'Cine registrado exitosamente.'
        })
    return render(request,'gestionCines.html')



def vista_cines(request):
    cines = Cine.objects.all()  # Asegúrate de que 'Cine' es tu modelo
    return render(request, 'listadoCines.html', {'cine': cines})


