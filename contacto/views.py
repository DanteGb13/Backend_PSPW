# En views.py

from django.shortcuts import render, redirect
from .forms import FormularioContacto
from .models import MensajeContacto

def contacto(request):
    if request.method == 'POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('contacto?valido=True')  # Redirecciona a la misma página con parámetro de éxito
    else:
        formulario = FormularioContacto()

    return render(request, 'tu_app/contacto.html', {'miFormulario': formulario})
