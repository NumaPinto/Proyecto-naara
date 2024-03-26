from django.db import models

# Create your models here.

class Catalogo(models.Model):

    nombre_articulo=  models.CharField(max_length=30)
    #fecha = models.DateField() # campo de fecha
   
