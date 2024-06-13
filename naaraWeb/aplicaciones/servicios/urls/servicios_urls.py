"""
URL configuration for naaraWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from aplicaciones.servicios.vistas.servicios_citas_views import CitasCreateView, OpeningView, ReservaListView, ClienteListView
from aplicaciones.servicios.vistas.servicios_equipo_views import TeamView
from aplicaciones.servicios.vistas.servicios_inicio_views import InicioView
from aplicaciones.servicios.vistas.servicios_nosotros_views import AboutView, ContactView, SuscribirView, ContactarView
from aplicaciones.servicios.vistas.servicios_ventas_views import PriceView, AppointmentView, ServicioListView, ProductoListView

urlpatterns = [

     # URLs para la informacion
    path('', InicioView.as_view(),name='index'),
    path('about/', AboutView.as_view(),name='about'),
    path('price/', PriceView.as_view(),name='price'),
    path('appointment/', AppointmentView.as_view(),name='appointment'),
    path('contact/', ContactView.as_view(),name='contact'),
    path('opening/', OpeningView.as_view(),name='opening'),
    path('team/', TeamView.as_view(),name='team'),
 
    
    # URLs para los servicios
    path('servicios/', ServicioListView.as_view(), name='servicio-list'),

    # URLs para los productos
    path('productos/', ProductoListView.as_view(), name='producto-list'),

    # URLs para las reservas
    path('reservas/', ReservaListView.as_view(), name='reserva-list'),

    # URLs para los clientes
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    
    path('citas/', CitasCreateView.as_view(), name='citas'),
    
    path('suscribirse/',SuscribirView.as_view(), name = 'suscribirse'),
    
    path('contactanos/',ContactarView.as_view(), name = 'contactanos'),
]