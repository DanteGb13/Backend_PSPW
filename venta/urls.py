# venta/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('carrito', views.menu, name='carrito'),
    path('clima', views.clima, name='clima'),
    path('contacto', views.contacto, name='contacto'),
    path('logear', views.logear, name='logear'),
    path('Autenticacion', views.Autenticacion, name='Autenticacion'),
    path('zapatilla', views.zapatilla, name='zapatilla'),
    path('zapatillas', views.zapatillas, name='zapatillas'),
    # otras rutas de la aplicación 'venta'
]
