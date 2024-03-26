from django.contrib import admin

from catalogo.models import Catalogo

# Register your models here.

class CatalogoAdministracion(admin.ModelAdmin):
    list_display = ["nombre_articulo"]
    search_fields = ["nombre_articulo"]
    list_filter = ["nombre_articulo"]
    #date_hierarchy ="fecha" #Para campos de fecha
    

admin.site.register(Catalogo,CatalogoAdministracion)