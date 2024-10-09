# views.py
from rest_framework import generics
from aplicaciones.servicios.modelos.servicios_ventas_models import Servicio
from aplicaciones.servicios.serializadores.servicios_ventas_serializers import ServicioSerializer

class ServicioListCreateView(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
