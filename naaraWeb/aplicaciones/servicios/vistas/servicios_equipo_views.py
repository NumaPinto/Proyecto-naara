from django.shortcuts import render
from django.views.generic import TemplateView
from aplicaciones.servicios.modelos.servicios_atencion_models import Especialistas

class TeamView(TemplateView):

    template_name = "team.html"
    
    def get(self,request,*args,**kwargs): 
        
        informacion_especialistas = self.__get_informacion_especilistas()
        
        resultado = {"datos_especialista":informacion_especialistas}

        return render(request,self.template_name,resultado)
    
    def __get_informacion_especilistas(self):
      
     datos =  list(Especialistas.objects.filter(estado=True))
     
     return datos