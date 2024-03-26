from django.shortcuts import render
from django.views.generic import View

#Vista basada en clase
class Inicio(View):

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo
        return render(request,"index.html")

#Vista basada en clase
class Inicio(View):

    def get(self,request,*args,**kwargs): #Sobreescribiendo metodo
        return render(request,"index.html")

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

