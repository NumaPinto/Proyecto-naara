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
     
     especialistas = []
     
     for i in range(len(datos)):
      
       if datos[i].nombre_especialista.startswith("Dr.") or datos[i].nombre_especialista.startswith("Dra."):
        
         informacion.append(datos[i])
     
     for n in range(len(informacion)):
  
       if informacion[n].nombre_especialista.startswith("Dr."):

         especialistas.append(informacion[n])
         
     for m in range(len(informacion)):
                     
         if informacion[m].nombre_especialista.startswith("Dra."):
           
           especialistas.append(informacion[m])
          
     for a in range(len(datos)):
       
       if datos[a].especialidad_especialista.startswith("Enfermera"):
         
       
         especialistas.append(datos[a])
       
     for b in range(len(datos)):
       
       if datos[b].especialidad_especialista.startswith("Cosmetóloga"):
       
         especialistas.append(datos[b])

       
     for c in range(len(datos)):
       
       if datos[c].especialidad_especialista.startswith("Masoterapeuta"):
       
         especialistas.append(datos[c])

       
     for d in range(len(datos)):
       
       if datos[d].especialidad_especialista.startswith("Estilista"):
         
         especialistas.append(datos[d])

       
     for f in range(len(datos)):
       
       if datos[f].especialidad_especialista.startswith("Manicurista"):
       
         especialistas.append(datos[f])
       
     for g in range(len(datos)):
       
       if datos[g].especialidad_especialista.startswith("Atención al Cliente"):
       
         especialistas.append(datos[g])
       
     return especialistas
     