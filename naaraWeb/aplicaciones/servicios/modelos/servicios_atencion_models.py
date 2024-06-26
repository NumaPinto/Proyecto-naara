from django.db import models
from aplicaciones.servicios.modelos.servicios_base_models import ModeloBase

'''Modelo que se encarga de registrar todos los especialistas de la empresa''' 
class Especialistas(ModeloBase):
    nombre_especialista = models.CharField("Nombre",max_length=100)
    apellido_especialista = models.CharField("Apellido",max_length=100)
    especialidad_especialista = models.CharField("Especialidad",max_length=100)
    telefono_especialista = models.CharField("Teléfono",max_length=15)
    correo_especialista = models.EmailField("Correo")
    foto_especialista= models.ImageField("Foto",upload_to="servicios/fotos/especialistas/", blank=True, null=True)
    web =models.URLField("Pagina Web", null=True,blank=True)
    facebook =models.URLField("Facebook", null=True,blank=True)
    instagram =models.URLField("Instagram", null=True,blank=True)
    youtube =models.URLField("YouTube", null=True,blank=True)
    class Meta:
      verbose_name="Especialista"
      verbose_name_plural="Especialistas"

    def __str__(self):
        return f'{self.nombre_especialista} {self.apellido_especialista}'
        
'''Modelo que se encarga de registrar informacion adicional de la pagina'''
class InformacionPagina(ModeloBase):
    informacion = models.CharField("Información de la página Web",max_length=300)
    acerca = models.TextField("Acerca de la página Web")
    facebook =models.URLField("Facebook", null=True,blank=True)
    instagram =models.URLField("Instagram", null=True,blank=True)
    youtube =models.URLField("YouTube", null=True,blank=True)
    
    class Meta:
      verbose_name="Informacion de la Pagina Web"
      verbose_name_plural="Informacion de la Pagina Web"
    
    def __str__(self):
        return self.informacion