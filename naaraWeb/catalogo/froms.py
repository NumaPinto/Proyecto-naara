from django import forms
from .models import Citas

class CitasForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = ['nombre', 'correo', 'fecha', 'hora', 'servicio']
        CHOICES = (('Option 1', 'Option 1'),
               ('Option 2', 'Option 2'),)
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control bg-transparent p-4 datetimepicker-input', 'placeholder': 'Fecha', 'data-target': '#date', 'data-toggle': 'datetimepicker'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control bg-transparent p-4 datetimepicker-input', 'placeholder': 'Hora', 'data-target': '#time', 'data-toggle': 'datetimepicker'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-transparent p-4', 'placeholder': 'Nombres'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control bg-transparent p-4', 'placeholder': 'Correo'}),
            'servicio': forms.Select(choices=CHOICES,attrs={'class': 'custom-select bg-transparent px-4', 'style': 'height: 47px;','option':'Elegir Servicios'}),
        }