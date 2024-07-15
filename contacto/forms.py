# En forms.py (puede crear este archivo si no existe)

from django import forms
from .models import MensajeContacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'mensaje']
