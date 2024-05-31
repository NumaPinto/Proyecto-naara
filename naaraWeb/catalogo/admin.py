from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Servicio, Producto, Reserva, Cliente,InformacionPagina
from .models import Especialistas, Planes, Citas,Suscriptor, Contactanos


class SuscriptorResource(resources.ModelResource):
    class Meta:
        model = Suscriptor


class ServicioResource(resources.ModelResource):
    class Meta:
        model = Servicio

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

class ReservaResource(resources.ModelResource):
    class Meta:
        model = Reserva
        
class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente
        
class InformacionPaginaResource(resources.ModelResource):
    class Meta:
        model = InformacionPagina
        
class EspecialistasResource(resources.ModelResource):
    class Meta:
        model = Especialistas
        
class PlanesResource(resources.ModelResource):
    class Meta:
        model = Planes
    
class CitasResource(resources.ModelResource):
    class Meta:
        model = Citas
        
class ContactanosResource(resources.ModelResource):
    class Meta:
        model = Contactanos
        
class SuscriptorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('correo','estado','fecha_de_creacion')
    search_fields = ['correo']
    resource_class = SuscriptorResource
    
class ServicioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre_servicio','estado','fecha_de_creacion','descripcion_servicio','precio_servicio')
    search_fields = ['nombre_servicio']
    resource_class = ServicioResource
    
class InformacionPaginaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('informacion','estado','fecha_de_creacion','acerca')
    search_fields = ['fecha_de_creacion']
    resource_class = InformacionPaginaResource
    
class EspecialistasAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre_especialista','apellido_especialista','estado','fecha_de_creacion','especialidad_especialista')
    search_fields = ['nombre_especialista','apellido_especialista','telefono_especialista']
    resource_class = EspecialistasResource
    
        
class CitasAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre','correo','fecha','hora','estado','fecha_de_creacion')
    search_fields = ['nombre','correo']
    resource_class = CistasResource



admin.site.register(Servicio,ServicioAdmin) 
admin.site.register(Producto)
admin.site.register(Reserva)
admin.site.register(Cliente)
admin.site.register(InformacionPagina,InformacionPaginaAdmin)
admin.site.register(Especialistas,EspecialistasAdmin)
admin.site.register(Planes)
admin.site.register(Citas,CitasAdmin)
admin.site.register(Suscriptor,SuscriptorAdmin)
admin.site.register(Contactanos,ContactanosAdmin)
    
