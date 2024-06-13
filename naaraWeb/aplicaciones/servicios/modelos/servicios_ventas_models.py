from django.db import models
from aplicaciones.servicios.modelos.servicios_base_models import ModeloBase

'''Modelo que se encarga de registrar los servicios de la empresa'''
class Servicio(ModeloBase):
    nombre_servicio = models.CharField("Nombre del Servicio",max_length=100)
    descripcion_servicio = models.TextField("Descripción del Servicio")
    precio_servicio = models.DecimalField("Precio del Servicio",max_digits=10, decimal_places=2)
    imagen_servicio = models.ImageField("Imagen del Servicio",upload_to="servicios/imagenes/servicios/", blank=True, null=True)
    
    class Meta:
      verbose_name="Servicio"
      verbose_name_plural="Servicios"

    def __str__(self):
        return self.nombre_servicio
    
'''Modelo que se encarga de registrar los productos de la empresa'''
class Producto(ModeloBase):
    nombre_producto = models.CharField("Nombre del Producto",max_length=100)
    descripcion_producto = models.TextField("Descripción del Producto")
    precio_producto = models.DecimalField("Precio del Producto",max_digits=10, decimal_places=2)
    cantidad_disponible_producto = models.PositiveIntegerField("Cantidad de Productos")
    imagen_producto = models.ImageField("Imagen del Producto",upload_to="servicios/imagenes/productos/", blank=True, null=True)
    
    class Meta:
      verbose_name="Producto"
      verbose_name_plural="Productos"

    def __str__(self):
        return self.nombre_producto


'''Modelo que se encarga de registrar los planes disponibles que ofrece la empresa'''
class Planes(ModeloBase):
    nombre_plan = models.CharField("Nombre del Plan",max_length=100)
    descripcion_plan = models.TextField("Descripción del Plan")
    precio_plan = models.DecimalField("Precio del Plan",max_digits=10, decimal_places=2)
    
    class Meta:
      verbose_name="Plan"
      verbose_name_plural="Planes"

    def __str__(self):
        return self.nombre_plan
    

