from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from aplicaciones.servicios.modelos.servicios_ventas_models import Servicio
from aplicaciones.servicios.modelos.servicios_usuarios_models import Citas
from aplicaciones.servicios.modelos.servicios_atencion_models import Especialistas, InformacionPagina
from aplicaciones.servicios.formularios.servicios_citas_froms import CitasForm

'''Clase que gestiona el formulario de las Citas  '''
class FormularioCitas(object):
    
    def get_formulario_citas(self):
        
        formulario_citas = CitasForm()
        
        return formulario_citas


'''Vista que se escarga de renderizar el inicio de la pagina y pasa alguna informacion adicional'''
class InicioView(CreateView):
  
    model = Especialistas

    template_name = "index.html"
    
    success_url = reverse_lazy('citas:success')
    
#Sobrescribiendo el metodo get de la super clase
    def get(self,request,*args,**kwargs): 
        
        informacion_especialistas = self.__get_informacion_especilistas(self.model)
        
        informacion_servicio = self.__get_informacion_servicios()
        
        informacion_pagina = self.__get_informacion_pagina()
        
    
        formulario_citas = FormularioCitas().get_formulario_citas()
        

        resultado = {"datos_especialista":informacion_especialistas,"form":formulario_citas,"datos_servicio":informacion_servicio,"datos_pagina":informacion_pagina}

        return render(request,self.template_name,resultado)
        
    def __get_informacion_especilistas(self,modelo):
      
     datos =  list(modelo.objects.filter(estado=True))
     
     informacion =[]

     if len(datos) >= 5:
     
        for i in range(5):
          
          informacion.append(datos[i])
        
     return informacion
     
    def __get_informacion_servicios(self):
        
        
        datos =  list(Servicio.objects.filter(estado=True))
        
        informacion =[]

        if len(datos) >= 6:
            for i in range(6):
                informacion.append(datos[i])
        
        return informacion
        
    def __get_informacion_pagina(self):
        
        
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