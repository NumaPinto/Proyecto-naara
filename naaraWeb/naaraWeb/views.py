from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import Template, context, loader

# Prueba

class Persona(object):

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido=apellido

def index(request):

    persona = Persona("Daniel","Diamon")
    
    datos = {"nombre_persona":persona.nombre,"apellido_persona":persona.apellido}

    #documento_html = loader.get_template("index.html")

    #documento_web = documento_html.render(datos)

    #return HttpResponse(documento_web)

    return render(request,"index.html",datos)


def servicios(request):

    persona = Persona("Daniel","Diamon")
    
    datos = {"nombre_persona":persona.nombre,"apellido_persona":persona.apellido}

    return render(request,"servicios.html",datos)

def galeria(request):

    persona = Persona("Daniel","Diamon")
    
    datos = {"nombre_persona":persona.nombre,"apellido_persona":persona.apellido}

    return render(request,"galeria.html",datos)

def contacto(request):

    persona = Persona("Daniel","Diamon")
    
    datos = {"nombre_persona":persona.nombre,"apellido_persona":persona.apellido}

    return render(request,"contacto.html",datos)