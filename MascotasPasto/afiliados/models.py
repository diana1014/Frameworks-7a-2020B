from django.db import models
# Create your models here.

class Paises(models.Model):
    ide= models.CharField(max_length=10, primary_key=True)
    code= models.CharField(max_length=10)
    nombre= models.CharField(max_length=100)
    abreviatura= models.CharField(max_length=100)
    estado= models.CharField(max_length=100)
    fecha_creacion= models.CharField(max_length=100)
    fecha_modificacion= models.CharField(max_length=100)


class Ciudades(models.Model):
    ide= models.CharField(max_length=10, primary_key=True)
    code= models.CharField(max_length=10)
    nombre= models.CharField(max_length=100)
    abreviatura= models.CharField(max_length=100)
    id_pais= models.ForeignKey(Paises,on_delete= models.CASCADE)
    estado= models.CharField(max_length=100)
    fecha_creacion= models.CharField(max_length=100)
    fecha_modificacion= models.CharField(max_length=100)

class Afiliados(models.Model):
    code= models.CharField(max_length=10)
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    direccion= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    ide_ciudad= models.ForeignKey(Ciudades,on_delete=models.CASCADE)
    estado= models.CharField(max_length=100)
    fecha_creacion= models.CharField(max_length=100)
    fecha_modificacion= models.CharField(max_length=100)



    