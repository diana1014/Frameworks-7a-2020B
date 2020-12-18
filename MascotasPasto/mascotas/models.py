from django.db import models

class Mascotas (models.Model):
    ide= models.CharField(max_length=10)
    codigo= models.CharField(max_length=10)
    ide_tipo= models.CharField(max_length=10)
    ide_raza= models.CharField(max_length=10)
    nombre= models.CharField(max_length=100)
    tiene_vacunas= models.CharField(max_length=100)
    estado= models.CharField(max_length=100)
    fecha_creacion= models.CharField(max_length=100)
    fecha_modificacion= models.CharField(max_length=100)

class Tipos (models.Model):
    ide= models.CharField(max_length=10)
    code= models.CharField(max_length=10)
    nombre= models.CharField(max_length=100)
    abreviatura= models.CharField(max_length=100)
    estado= models.CharField(max_length=100)
    fecha_creacion= models.CharField(max_length=100)
    fecha_modificacion= models.CharField(max_length=100)

class Razas (models.Model):
    ide= models.CharField(max_length=10)
    code= models.CharField(max_length=10)
    nombre= models.CharField(max_length=100)
    abreviatura= models.CharField(max_length=100)
    id_tipo= models.CharField(max_length=10)
    estado= models.CharField(max_length=100)
    fecha_creacion= models.CharField(max_length=100)
    fecha_modificacion= models.CharField(max_length=100)
    