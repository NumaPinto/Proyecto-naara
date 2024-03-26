from django.contrib import admin
from .models import Servicio, Producto, Reserva, Cliente

admin.site.register(Servicio)
admin.site.register(Producto)
admin.site.register(Reserva)
admin.site.register(Cliente)
    
