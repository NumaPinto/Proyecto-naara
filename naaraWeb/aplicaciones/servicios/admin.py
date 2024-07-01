from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from aplicaciones.servicios.modelos.servicios_ventas_models import Servicio, Producto, Planes
from aplicaciones.servicios.modelos.servicios_usuarios_models import Cliente, Reserva, Contactanos, Citas, Suscriptor
from aplicaciones.servicios.modelos.servicios_atencion_models import Especialistas, InformacionPagina


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
    list_display = ('nombre_servicio','estado','fecha_de_creacion','descripcion_servicio','precio_servicio','imagen')
    search_fields = ['nombre_servicio']
    resource_class = ServicioResource
    
    def imagen(self,obj):
      return format_html('<img src = {} width = "130" height = "100"> </img>', obj.imagen_servicio.url)
   
class InformacionPaginaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('informacion','estado','fecha_de_creacion','acerca')
    search_fields = ['fecha_de_creacion']
    resource_class = InformacionPaginaResource
    
class EspecialistasAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre_especialista','apellido_especialista','estado','fecha_de_creacion','especialidad_especialista','foto')
    search_fields = ['nombre_especialista','apellido_especialista','telefono_especialista']
    resource_class = EspecialistasResource
    
    def foto(self,obj):
      return format_html('<img src = {} width = "130" height = "100"> </img>', obj.foto_especialista.url)

class ContactanosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre_cliente','apellido_cliente','telefono_cliente','asunto_cliente','mensaje_cliente','estado','fecha_de_creacion')
    search_fields = ['nombre_cliente','apellido_cliente','telefono_cliente']
    resource_class = ContactanosResource
    
class CitasAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre','correo','fecha','hora','estado','fecha_de_creacion')
    search_fields = ['nombre','correo']
    resource_class = CitasResource

class ProductoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre_producto','descripcion_producto','precio_producto','cantidad_disponible_producto','estado','fecha_de_creacion','imagen')
    search_fields = ['nombre_producto','precio_producto']
    resource_class = ProductoResource
    
    def imagen(self,obj):
      return format_html('<img src = {} width = "130" height = "100"> </img>', obj.imagen_producto.url)

class PlanesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre_plan','descripcion_plan','precio_plan','estado','fecha_de_creacion')
    search_fields = ['nombre_plan','precio_plan']
    resource_class = PlanesResource

class ReservaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre_cliente','fecha','telefono_cliente','correo_cliente','estado','fecha_de_creacion')
    search_fields = ['nombre_cliente','fecha']
    resource_class = ReservaResource

class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre_cliente','apellido_cliente','telefono_cliente','correo_cliente','estado','fecha_de_creacion')
    search_fields = ['nombre_cliente','apellido_cliente','telefono_cliente','correo_cliente']
    resource_class = ClienteResource

admin.site.register(Servicio,ServicioAdmin) 
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(InformacionPagina,InformacionPaginaAdmin)
admin.site.register(Especialistas,EspecialistasAdmin)
admin.site.register(Planes,PlanesAdmin)
admin.site.register(Citas,CitasAdmin)
admin.site.register(Suscriptor,SuscriptorAdmin)
admin.site.register(Contactanos,ContactanosAdmin)
    