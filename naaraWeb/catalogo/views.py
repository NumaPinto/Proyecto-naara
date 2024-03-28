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

    template_name = "index.html"

    def get(self,request,*args,**kwargs): #Sobrescribiendo el metodo get de la super clase

        informacion = InformacionPagina.objects.all()

        informacion_servicios = Servicio.objects.all()

        informacion_especialistas = Especialistas.objects.all()

        resultado = {"datos":informacion,"datos_servicio":informacion_servicios,"datos_especialistas":informacion_especialistas}

        return render(request,self.template_name,resultado)

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

class Testimonial(TemplateView):

     template_name = "testimonial.html"


class ServicioListView(ListView):
    model = Servicio
    template_name ="service.html"
    context_object_name ="datos"

class ServicioDetailView(DetailView):
    #template_name ="servicio_detail.html"
    model = Servicio

class ServicioCreateView(CreateView):
    model = Servicio
   # template_name ="servicio_form.html"
    fields = ['nombre_servicio', 'descripcion_servicio', 'precio_servicio']

class ServicioUpdateView(UpdateView):
    model = Servicio
   # template_name ="servicio_form.html"
    fields = ['nombre_servicio', 'descripcion_servicio', 'precio_servicio']

class ServicioDeleteView(DeleteView):
    model = Servicio
   # template_name ="servicio_confirm_delete.html"
    success_url = reverse_lazy('servicio-list')

class ProductoListView(ListView):
    model = Producto

class ProductoDetailView(DetailView):
    model = Producto

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre_producto', 'descripcion_producto', 'precio_producto', 'cantidad_disponible_producto']

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre_producto', 'descripcion_producto', 'precio_producto', 'cantidad_disponible_producto']

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto-list')

class ReservaListView(ListView):
    model = Reserva

class ReservaDetailView(DetailView):
    model = Reserva

class ReservaCreateView(CreateView):
    model = Reserva
    fields = ['servicio', 'productos', 'fecha', 'nombre_cliente', 'telefono_cliente', 'correo_cliente']

class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = ['servicio', 'productos', 'fecha', 'nombre_cliente', 'telefono_cliente', 'correo_cliente']

class ReservaDeleteView(DeleteView):
    model = Reserva
    success_url = reverse_lazy('reserva-list')

class ClienteListView(ListView):
    model = Cliente

class ClienteDetailView(DetailView):
    model = Cliente

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre_cliente', 'apellido_cliente', 'telefono_cliente', 'correo_cliente']

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre_cliente', 'apellido_cliente', 'telefono_cliente', 'correo_cliente']

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente-list')
