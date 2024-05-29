from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView,FormView
from .models import Servicio, Producto, Reserva, Cliente,InformacionPagina,Especialistas, Citas
from django.urls import reverse_lazy
from .frams import CitasForm



class ReservaCita(FormView):
    template_name = 'index.html'
    form_class = CitasForm
    success_url = reverse_lazy('appointment_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


'''Vista que se escarga de renderizar el inicio de la pagina y pasa alguna informacion adicional'''
class Inicio(TemplateView):
  
    model = Especialistas()

    template_name = "index.html"
    
#Sobrescribiendo el metodo get de la super clase
    def get(self,request,*args,**kwargs): 

        informacion_servicios = Servicio.objects.all()
        informacion_especialistas = self._get_informacion_especilistas(self.model)

        resultado = {"datos_especialista":informacion_especialistas}

        return render(request,self.template_name,resultado)
    def _get_informacion_especilistas(self,modelo):
      
     informacion =  modelo.objects.filter(estado=True)
     
     
     return informacion

class About(TemplateView):

    template_name = "about.html"

class Price(TemplateView):

    template_name = "price.html"


class Appointment(TemplateView):

    template_name = "appointment.html"
    

class Opening(TemplateView):

    template_name = "opening.html"

    
class Team(TemplateView):

    template_name = "team.html"


class Contact(TemplateView):

    template_name = "contact.html"

class ServicioListView(ListView):
    model = Servicio
    template_name ="service.html"

class ProductoListView(ListView):
    model = Producto

class ReservaListView(ListView):
    model = Reserva

class ClienteListView(ListView):
    model = Cliente

