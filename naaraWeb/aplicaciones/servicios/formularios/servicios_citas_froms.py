from django import forms
from aplicaciones.servicios.modelos.servicios_usuarios_models import Citas

class CitasForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = ['nombre', 'correo', 'fecha', 'hora', 'servicio']
        widgets = {
            'fecha': forms.DateInput(attrs={
                'class': 'form-control bg-transparent p-4',
                'placeholder': 'Fecha',
                'type': 'date'
            }),
            'hora': forms.TimeInput(attrs={
                'class': 'form-control bg-transparent p-4',
                'placeholder': 'Hora',
                'type': 'time'
            }),
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-transparent p-4', 'placeholder': 'Nombres'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control bg-transparent p-4', 'placeholder': 'Correo'}),
            'servicio': forms.Select(attrs={'class': 'custom-select bg-transparent px-4', 'style': 'height: 47px;', 'option': 'Elegir Servicios'}),
        }
