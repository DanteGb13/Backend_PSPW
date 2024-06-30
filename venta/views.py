from django.shortcuts import render
# Create your views here.

def menu(request):
    return render(request, 'menu.html')  # Asegúrate de que esta ruta sea correcta

