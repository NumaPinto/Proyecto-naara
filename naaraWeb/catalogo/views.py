from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Servicio, Producto, Reserva, Cliente,InformacionPagina
from django.urls import reverse_lazy
"""from django.views.generic import View, TemplateView, ListView
from catalogo.models import Catalogo
"""
"""#Vista basada en clase
class Inicio(View):

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo
        return render(request,"index.html")"""
"""
#Vista basada en clase, esta clase solo renderiza una plantilla
class Inicio(TemplateView):

    template_name = "index.html"
"""

""""#Vista basada en clase
class ListaNombres(TemplateView):

    template_name ="lista.html"

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo

        #nombres = Catalogo.objects.filter(nombre_articulo=True)

        nombres = Catalogo.objects.all()

        resultado = {"datos":nombres}

        return render(request,self.template_name,resultado)"""
"""
#Vista basada en clase, se usa para listar
class ListaNombres(ListView):

    model = Catalogo

    template_name ="lista.html"

    context_object_name ="datos"

    queryset = Catalogo.objects.all()

    #queryset = Catalogo.objects.all() #Esto esta interno por defecto


#Vista basada en clase
class Precio(View):

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo
        return render(request,"price.html")
    
#Vista basada en clase
class Servicio(View):

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo
        return render(request,"service.html")
    
#Vista basada en clase
class Appointment(View):

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo
          return render(request,"appointment.html")
    
#Vista basada en clase
class Opening(View):

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo
        return render(request,"opening.html")
    
#Vista basada en clase
class Team(View):

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo
        return render(request,"team.html")


#Vista basada en clase
class About(View):

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo
       return render(request,"about.html")

#Vista basada en clase
class Contact(View):

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo
        return render(request,"contact.html")

#Vista basada en clase
class Testimonial(View):

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo
        return render(request,"testimonial.html")

"""

class Inicio(TemplateView):

    template_name = "index.html"

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo

        informacion = InformacionPagina.objects.all()

        informacion_servicio = Servicio.objects.all()

        resultado = {"datos":informacion,"datos_servicio":informacion_servicio}

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
