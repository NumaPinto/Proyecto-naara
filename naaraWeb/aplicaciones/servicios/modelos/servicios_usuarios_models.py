from django.db import models
from aplicaciones.servicios.modelos.servicios_base_models import ModeloBase
from aplicaciones.servicios.modelos.servicios_ventas_models import Servicio, Producto

'''Modelo que se encarga de registrar las resrvas de los clientes'''
class Reserva(ModeloBase):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, blank=True)
    fecha = models.DateTimeField("Fecha")
    nombre_cliente = models.CharField("Nombre del Cliente",max_length=100)
    telefono_cliente = models.CharField("Teléfono del Cliente",max_length=15)
    correo_cliente = models.EmailField("Correo")
    
    class Meta:
      verbose_name="Reserva"
      verbose_name_plural="Reservas"

    def __str__(self):
        return f'Reserva de {self.servicio.nombre} para {self.nombre_cliente}'
    
'''Modelo que se encarga de registrar la informacion de los clientes'''
class Cliente(ModeloBase):
    nombre_cliente = models.CharField("Nombre del Cliente",max_length=100)
    apellido_cliente = models.CharField("Apellido del Cliente",max_length=100)
    telefono_cliente = models.CharField("Teléfono del Cliente",max_length=15)
    correo_cliente = models.EmailField("Correo")
    
    class Meta:
      verbose_name="Cliente"
      verbose_name_plural="Clientes"

    def __str__(self):
        return f'{self.nombre_cliente} {self.apellido_cliente}'

    
'''Modelo que se encarga de registrar las citas de los clientes''' 
class Citas(ModeloBase):
    nombre = models.CharField("Nombre del Cliente",max_length=100)
    correo = models.EmailField("Correo")
    fecha = models.DateField("Fecha")
    hora = models.TimeField("Hora")
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    
    class Meta:
      verbose_name="Cita"
      verbose_name_plural="Citas"

    def __str__(self):
        return self.nombre
        

'''Modelo que se encarga de registrar la informacion de los usuarios'''
class Contactanos(ModeloBase):
    nombre_cliente = models.CharField("Nombre del Cliente",max_length=100)
    apellido_cliente = models.CharField("Apellido del Cliente",max_length=100)
    telefono_cliente = models.CharField("Teléfono del Cliente",max_length=15)
    correo_cliente = models.EmailField("Correo")
    asunto_cliente = models.CharField("Asunto",max_length=100)
    mensaje_cliente = models.TextField("Mensaje")
    
    class Meta:
      verbose_name="Contacto"
      verbose_name_plural="Contactanos"

    def __str__(self):
        return f'{self.nombre_cliente} {self.apellido_cliente}'


class Suscriptor(ModeloBase):
    correo = models.EmailField('Correo Electrónico', max_length = 200)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.correo