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
from catalogo.views import Inicio, About, Appointment, Contact, Opening, Precio, Servicio, Team, Testimonial

urlpatterns = [
    path('', Inicio.as_view(),name='index'),
    path('about/', About.as_view(),name='about'),
    path('appointment/', Appointment.as_view(),name='appointment'),
    path('contact/', Contact.as_view(),name='contact'),
    path('opening/', Opening.as_view(),name='opening'),
    path('price/', Precio.as_view(),name='price'),
    path('service/', Servicio.as_view(),name='service'),
    path('team/', Team.as_view(),name='team'),
    path('testimonial/', Testimonial.as_view(),name='testimonial'),
  
]
