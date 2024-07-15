# En tu aplicación Django, en un archivo models.py

from django.db import models

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
