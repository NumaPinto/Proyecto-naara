from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy
from aplicaciones.servicios.modelos.servicios_usuarios_models import Reserva,Cliente, Citas
from aplicaciones.servicios.formularios.servicios_citas_froms import CitasForm

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

class OpeningView(TemplateView):

    template_name = "opening.html"
    
class ReservaListView(ListView):
    model = Reserva
    
class ClienteListView(ListView):
    model = Cliente
