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
     
     informacion = []
     
     doctores = []
     
     for i in range(len(datos)):
      
       if datos[i].nombre_especialista.startswith("Dr.") or datos[i].nombre_especialista.startswith("Dra."):
        
            informacion.append(datos[i])
            
            for n range(len(informacion)):
              
              if informacion[n].nombre_especialista.startswith("Dra."):
               
                doctores.append(informacion[n])
              else:
                doctores.append(informacion[n])
              
     for j in range(len(datos)):
       
       if datos[j].nombre_especialista.startswith("Dr.") or datos[j].nombre_especialista.startswith("Dra."):
         
         nada = []
        
       else:
 
          doctores.append(datos[j])
             
     return doctores
     