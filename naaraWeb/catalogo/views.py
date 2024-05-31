from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView,FormView,View
from .models import Servicio, Producto, Reserva, Cliente,InformacionPagina,Especialistas, Suscriptor, Contactanos, Citas
from django.urls import reverse_lazy
from .froms import CitasForm
from django.core.mail import send_mail
from naaraWeb.settings import EMAIL_HOST_USER


'''Clase que gestiona el formulario de las Citas  '''
class FormularioCitas(object):
    
    def getFormularioCitas(self):
        
        formulario_citas = CitasForm()
        
        return formulario_citas

class CitasCreateView(CreateView):
    model = Citas
    form_class = CitasForm
    template_name = 'index.html'
    success_url = reverse_lazy('citas:success')
    
    def post(self,request,*args,**kwargs):
            form = CitasForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                contexto = {
                    'form':form,
                }
                return render(request,'index.html',contexto)



'''Vista que se escarga de renderizar el inicio de la pagina y pasa alguna informacion adicional'''
class Inicio(CreateView):
  
    model = Especialistas

    template_name = "index.html"
    
    success_url = reverse_lazy('citas:success')
    
#Sobrescribiendo el metodo get de la super clase
    def get(self,request,*args,**kwargs): 
        
        informacion_especialistas = self._get_informacion_especilistas(self.model)
        
        informacion_servicio = self._get_informacion_servicios()
        
        informacion_pagina = self._get_informacion_pagina()
        

    
        formulario_citas = FormularioCitas().getFormularioCitas()
        
        

        resultado = {"datos_especialista":informacion_especialistas,"form":formulario_citas,"datos_servicio":informacion_servicio,"datos_pagina":informacion_pagina}

        return render(request,self.template_name,resultado)
        
    def _get_informacion_especilistas(self,modelo):
      
     datos =  list(modelo.objects.filter(estado=True))
     
     informacion =[]

     if len(datos) >= 5:
     
        for i in range(5):
          
          informacion.append(datos[i])
        
    
     return informacion
     
    def _get_informacion_servicios(self):
        
        
        datos =  list(Servicio.objects.filter(estado=True))
        
        informacion =[]

        if len(datos) >= 6:
            for i in range(6):
                informacion.append(datos[i])
        
        
        
        
        return informacion
        
        
        
    def _get_informacion_pagina(self):
        
        
        datos =  list(InformacionPagina.objects.filter(estado=True))
        

        return datos
     
     
        
     
    def post(self,request,*args,**kwargs):
            form = CitasForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                contexto = {
                    'form':form,
                }
                return render(request,'index.html',contexto)

         


class About(TemplateView):

    template_name = "about.html"
    
    def get(self,request,*args,**kwargs): 
        
        informacion_pagina = self._get_informacion_pagina()
        
        resultado = {"datos_pagina":informacion_pagina}

        return render(request,self.template_name,resultado)

    
    def _get_informacion_pagina(self):
        
        
        datos =  list(InformacionPagina.objects.filter(estado=True))
        

        return datos

    

class Price(TemplateView):

    template_name = "price.html"


class Appointment(TemplateView):

    template_name = "appointment.html"
    
    
    
    def post(self,request,*args,**kwargs):
            form = CitasForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                contexto = {
                    'form':form,
                }
                return render(request,'index.html',contexto)
                
    def get(self,request,*args,**kwargs):
        
    
         formulario_citas = FormularioCitas().getFormularioCitas()
        
         resultado = {"form":formulario_citas}

         return render(request,self.template_name,resultado)
    

class Opening(TemplateView):

    template_name = "opening.html"

    
class Team(TemplateView):

    template_name = "team.html"
    
    
    
    def get(self,request,*args,**kwargs): 
        
        informacion_especialistas = self._get_informacion_especilistas()
        
        resultado = {"datos_especialista":informacion_especialistas}

        return render(request,self.template_name,resultado)
    
    
    
    def _get_informacion_especilistas(self):
      
     datos =  list(Especialistas.objects.filter(estado=True))
     
     return datos


class Contact(TemplateView):

    template_name = "contact.html"

class ServicioListView(TemplateView):
 
    template_name ="service.html"
    
    
    def get(self,request,*args,**kwargs):
        
    
         formulario_citas = FormularioCitas().getFormularioCitas()
         
         informacion_servicio =self._get_informacion_servicios()
        
         resultado = {"form":formulario_citas,  "datos_servicio":informacion_servicio
                       }

         return render(request,self.template_name,resultado)
    
    
    def post(self,request,*args,**kwargs):
            form = CitasForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                contexto = {
                    'form':form,
                }
                return render(request,'index.html',contexto)
                
    def _get_informacion_servicios(self):
      
     datos =  list(Servicio.objects.filter(estado=True))
        
     print(len(datos))
    
     return datos
                

class Suscribir(View):
    def post(self,request,*args,**kwargs):
        correo = request.POST.get('correo')
        Suscriptor.objects.create(correo = correo)
        asunto = 'GRACIAS POR SUSCRIBIRTE A NAARA'
        mensaje = 'Te haz suscrito exitosamente a Naara, Gracias por tu preferencia!!!'
        try:
            send_mail(asunto,mensaje,EMAIL_HOST_USER,[correo])
        except:
            pass

        return redirect('index')
        
class Contactar(View):
    def post(self,request,*args,**kwargs):
        nombre_cliente =request.POST.get('nombre_cliente')
        apellido_cliente = request.POST.get('apellido_cliente')
        telefono_cliente = request.POST.get('telefono_cliente')
        correo_cliente = request.POST.get('correo_cliente')
        asunto_cliente = request.POST.get('asunto_cliente')
        mensaje_cliente = request.POST.get('mensaje_cliente')
        
        try:
          Contactanos.objects.create(nombre_cliente = nombre_cliente,apellido_cliente=apellido_cliente,telefono_cliente=telefono_cliente,correo_cliente=correo_cliente,asunto_cliente=asunto_cliente,mensaje_cliente=mensaje_cliente
          )
        except:
            pass

        return redirect('index')


class ProductoListView(ListView):
    model = Producto

class ReservaListView(ListView):
    model = Reserva

class ClienteListView(ListView):
    model = Cliente

