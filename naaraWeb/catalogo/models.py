from django.db import models

'''Modelo que se encarga de registrar los servicios de la empresa'''
class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion_servicio = models.TextField()
    precio_servicio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_servicio = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_servicio
    
'''Modelo que se encarga de registrar los productos de la empresa'''
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion_producto = models.TextField()
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible_producto = models.PositiveIntegerField()
    imagen_producto = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_producto

'''Modelo que se encarga de registrar las resrvas de los clientes'''
class Reserva(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, blank=True)
    fecha = models.DateTimeField()
    nombre_cliente = models.CharField(max_length=100)
    telefono_cliente = models.CharField(max_length=15)
    correo_cliente = models.EmailField()


    def __str__(self):
        return f'Reserva de {self.servicio.nombre} para {self.nombre_cliente}'
    
'''Modelo que se encarga de registrar la informacion de los clientes'''
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    telefono_cliente = models.CharField(max_length=15)
    correo_cliente = models.EmailField()

    def __str__(self):
        return f'{self.nombre_cliente} {self.apellido_cliente}'

'''Modelo que se encarga de registrar informacion adicional de la pagina'''
class InformacionPagina(models.Model):
    nombre_informacion = models.CharField(max_length=100)
    acerca = models.TextField()
    
    def __str__(self):
        return self.nombre_informacion

'''Modelo que se encarga de registrar los planes disponibles que ofrece la empresa'''
class Planes(models.Model):
    nombre_plan = models.CharField(max_length=100)
    descripcion_plan = models.TextField()
    precio_plan = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_plan
    
'''Modelo que se encarga de registrar todos los especialistas de la empresa''' 
class Especialistas(models.Model):
    nombre_especialista = models.CharField(max_length=100)
    apellido_especialista = models.CharField(max_length=100)
    especialidad_especialista = models.CharField(max_length=100)
    telefono_especialista = models.CharField(max_length=15)
    correo_especialista = models.EmailField()
    foto_especialista= models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre_especialista} {self.apellido_especialista}'
    
'''Modelo que se encarga de registrar las citas de los clientes''' 
class Citas(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha = models.DateField()
    hora = models.TimeField()
    servicio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
