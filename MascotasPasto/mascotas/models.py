from django.db import models

# Create your models here.
# Create your models here.
class Afiliados (models.Model):
    code= models.CharField(max_length=10)
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    direccion= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    id_ciudad= models.CharField(max_length=100)
    estado= models.CharField(max_length=100)
    fecha_creacion= models.CharField(max_length=100)
    fecha_modificacion= models.CharField(max_length=100)