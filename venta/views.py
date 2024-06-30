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

def login(request):
    return render(request, 'login.html') 

def signup(request):
    return render(request, 'signup.html') 

def zapatilla(request):
    return render(request, 'zapatilla.html') 

def zapatillas(request):
    return render(request, 'zapatillas.html') 