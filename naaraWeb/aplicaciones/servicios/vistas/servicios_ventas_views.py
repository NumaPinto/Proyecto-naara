from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from aplicaciones.servicios.modelos.servicios_ventas_models import Servicio, Producto
from aplicaciones.servicios.formularios.servicios_citas_froms import CitasForm

'''Clase que gestiona el formulario de las Citas  '''
class FormularioCitas(object):
    
    def get_formulario_citas(self):
        
        formulario_citas = CitasForm()
        
        return formulario_citas


class PriceView(TemplateView):

    template_name = "price.html"


class AppointmentView(TemplateView):

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
        
    
         formulario_citas = FormularioCitas().get_formulario_citas()
        
         resultado = {"form":formulario_citas}

         return render(request,self.template_name,resultado)
    

class ServicioListView(TemplateView):
 
    template_name ="service.html"
    
    
    def get(self,request,*args,**kwargs):
        
    
         formulario_citas = FormularioCitas().get_formulario_citas()
         
         informacion_servicio =self.__get_informacion_servicios()
        
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
                
    def __get_informacion_servicios(self):
      
     datos =  list(Servicio.objects.filter(estado=True))
        
    
     return datos
                

class ProductoListView(ListView):
    model = Producto