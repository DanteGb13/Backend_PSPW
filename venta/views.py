from django.shortcuts import render
# Create your views here.

def menu(request):
    return render(request, 'menu.html')  

def carrito(request):
    return render(request, 'carrito.html') 

def clima(request):
    return render(request, 'clima.html') 

def contacto(request):
    return render(request, 'contacto.html') 

def logear(request):
    return render(request, 'logear.html') 

def Autenticacion(request):
    return render(request, 'Autenticacion.html') 

def zapatilla(request):
    return render(request, 'zapatilla.html') 

def zapatillas(request):
    return render(request, 'zapatillas.html') 