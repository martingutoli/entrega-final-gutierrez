from django.db import models

# Create your models here.
class Alquileres (models.Model):
    tipo_de_operacion = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad_ambientes = models.IntegerField()
    cantidad_dormitorios = models.IntegerField()
    descripcion = models.CharField(max_length=100)

class Ventas (models.Model):
    tipo_de_operacion = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad_ambientes = models.IntegerField()
    cantidad_dormitorios = models.IntegerField()
    descripcion = models.CharField(max_length=100)
