from django.contrib import admin
from .models import Servicio, Producto, Reserva, Cliente,InformacionPagina
from .models import Especialistas, Planes, Citas

admin.site.register(Servicio)
admin.site.register(Producto)
admin.site.register(Reserva)
admin.site.register(Cliente)
admin.site.register(InformacionPagina)
admin.site.register(Especialistas)
admin.site.register(Planes)
admin.site.register(Citas)
    
