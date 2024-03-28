from django import forms
from .models import Citas

class CitasForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = ['nombre', 'correo', 'fecha', 'hora', 'servicio']