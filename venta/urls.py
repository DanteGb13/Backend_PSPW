# venta/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    # otras rutas de la aplicación 'venta'
]
