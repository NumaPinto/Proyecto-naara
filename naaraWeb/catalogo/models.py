from django.db import models


class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion_servicio = models.TextField()
    precio_servicio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_servicio = models.CharField(max_length=255, blank=True, null=True)



    def __str__(self):
        return self.nombre_servicio

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion_producto = models.TextField()
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible_producto = models.PositiveIntegerField()
    imagen_producto = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_producto

class Reserva(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, blank=True)
    fecha = models.DateTimeField()
    nombre_cliente = models.CharField(max_length=100)
    telefono_cliente = models.CharField(max_length=15)
    correo_cliente = models.EmailField()
    # Puedes agregar más campos según tus necesidades

    def __str__(self):
        return f'Reserva de {self.servicio.nombre} para {self.nombre_cliente}'
    
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    telefono_cliente = models.CharField(max_length=15)
    correo_cliente = models.EmailField()

    def __str__(self):
        return f'{self.nombre_cliente} {self.apellido_cliente}'
    
class InformacionPagina(models.Model):
    nombre_informacion = models.CharField(max_length=100)
    acerca = models.TextField()
    
    def __str__(self):
        return self.nombre_informacion
