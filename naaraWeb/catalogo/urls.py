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
from .views import ServicioListView
from .views import ProductoListView
from .views import ReservaListView
from .views import ClienteListView
from .views import Inicio, About, Price,Appointment, Contact, Opening, Team, Suscribir,Contactar
from .views import CitasCreateView

urlpatterns = [

     # URLs para la informacion
    path('', Inicio.as_view(),name='index'),
    path('about/', About.as_view(),name='about'),
    path('price/', Price.as_view(),name='price'),
    path('appointment/', Appointment.as_view(),name='appointment'),
    path('contact/', Contact.as_view(),name='contact'),
    path('opening/', Opening.as_view(),name='opening'),
    path('team/', Team.as_view(),name='team'),
 
    
    # URLs para los servicios
    path('servicios/', ServicioListView.as_view(), name='servicio-list'),

    # URLs para los productos
    path('productos/', ProductoListView.as_view(), name='producto-list'),

    # URLs para las reservas
    path('reservas/', ReservaListView.as_view(), name='reserva-list'),

    # URLs para los clientes
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    
    path('citas/', CitasCreateView.as_view(), name='citas'),
    
    path('suscribirse/',Suscribir.as_view(), name = 'suscribirse'),
    
    path('contactanos/',Contactar.as_view(), name = 'contactanos'),
]
