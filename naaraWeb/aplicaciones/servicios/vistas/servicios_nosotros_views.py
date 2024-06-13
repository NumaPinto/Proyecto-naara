from django.shortcuts import render, redirect
from django.views.generic import TemplateView,View
from django.core.mail import send_mail
from naaraWeb.settings import EMAIL_HOST_USER
from aplicaciones.servicios.modelos.servicios_usuarios_models import Contactanos, Suscriptor
from aplicaciones.servicios.modelos.servicios_atencion_models import InformacionPagina


class AboutView(TemplateView):

    template_name = "about.html"
    
    def get(self,request,*args,**kwargs): 
        
        informacion_pagina = self.__get_informacion_pagina()
        
        resultado = {"datos_pagina":informacion_pagina}

        return render(request,self.template_name,resultado)
    
    def __get_informacion_pagina(self):
        
        
        datos =  list(InformacionPagina.objects.filter(estado=True))
        

        return datos


class ContactView(TemplateView):

    template_name = "contact.html"
    
    
class SuscribirView(View):
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
        
class ContactarView(View):
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
