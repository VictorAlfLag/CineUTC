from django.db import models

#Creando un modelo Genero : Terror,Comedia,Accion


class Genero(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=150,default='')
    foto=models.FileField(upload_to='generos',null=True,blank=True)
    def __str__(self):
        #Para modificar las tables
        fila="{0} : {1} - {2} "
        return fila.format(self.id,self.nombre,self.descripcion)
        


class Director(models.Model):
    id=models.AutoField(primary_key=True)
    dni=models.CharField(max_length=15)
    apellido=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    estado=models.BooleanField(default=True)
    foto=models.FileField(upload_to='directores',null=True,blank=True)
    def __str__(self):
        #Para la modificacion y vista de las tablas
        fila = "{0} : {1} -- {2} -- {3} -- {4}"
        return fila.format(self.id,self.dni,self.apellido,self.nombre,self.estado)


class Pais(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    continente=models.CharField(max_length=30)
    capital=models.CharField(max_length=20)
    def __str__(self):
        fila= "{0} : {1} -- {2} -- {3}"
        return fila.format(self.id,self.nombre,self.continente,self.capital)


class Pelicula(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=250)
    duracion=models.TimeField(null=True)
    sinopsin=models.TextField()
    genero=models.ForeignKey(Genero,on_delete=models.CASCADE)
    Director=models.ForeignKey(Director,on_delete=models.CASCADE)
    Pais=models.ForeignKey(Pais,on_delete=models.CASCADE )
    def __str__(self):
        fila="{0}   :    {1}"
        return fila.format(self.id,self.titulo)
    

    
#Creando modelo Cine
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    direccion=models.CharField(max_length=150,default='')
    telefono=models.CharField(max_length=150,default='')
    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.direccion) 
    
