# serializers.py
from rest_framework import serializers
from aplicaciones.servicios.modelos.servicios_ventas_models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'estado', 'fecha_de_creacion', 'fecha_de_modificacion', 'fecha_de_eliminacion', 'nombre_servicio', 'descripcion_servicio', 'precio_servicio', 'imagen_servicio']
