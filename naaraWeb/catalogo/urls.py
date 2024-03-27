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
from .views import ServicioListView, ServicioDetailView, ServicioCreateView, ServicioUpdateView, ServicioDeleteView
from .views import ProductoListView, ProductoDetailView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView
from .views import ReservaListView, ReservaDetailView, ReservaCreateView, ReservaUpdateView, ReservaDeleteView
from .views import ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from .views import Inicio, About, Price,Appointment, Contact, Opening, Team, Testimonial

urlpatterns = [

     # URLs para la informacion
    path('', Inicio.as_view(),name='index'),
    path('about/', About.as_view(),name='about'),
    path('price/', Price.as_view(),name='price'),
    path('appointment/', Appointment.as_view(),name='appointment'),
    path('contact/', Contact.as_view(),name='contact'),
    path('opening/', Opening.as_view(),name='opening'),
    path('team/', Team.as_view(),name='team'),
    path('testimonial/', Testimonial.as_view(),name='testimonial'),
    
    # URLs para los servicios
    path('servicios/', ServicioListView.as_view(), name='servicio-list'),
    path('servicios/<int:pk>/', ServicioDetailView.as_view(), name='servicio-detail'),
    path('servicios/create/', ServicioCreateView.as_view(), name='servicio-create'),
    path('servicios/<int:pk>/update/', ServicioUpdateView.as_view(), name='servicio-update'),
    path('servicios/<int:pk>/delete/', ServicioDeleteView.as_view(), name='servicio-delete'),

    # URLs para los productos
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('productos/create/', ProductoCreateView.as_view(), name='producto-create'),
    path('productos/<int:pk>/update/', ProductoUpdateView.as_view(), name='producto-update'),
    path('productos/<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto-delete'),

    # URLs para las reservas
    path('reservas/', ReservaListView.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/', ReservaDetailView.as_view(), name='reserva-detail'),
    path('reservas/create/', ReservaCreateView.as_view(), name='reserva-create'),
    path('reservas/<int:pk>/update/', ReservaUpdateView.as_view(), name='reserva-update'),
    path('reservas/<int:pk>/delete/', ReservaDeleteView.as_view(), name='reserva-delete'),

    # URLs para los clientes
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/create/', ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/update/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='cliente-delete'),
]
