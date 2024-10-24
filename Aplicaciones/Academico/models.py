from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(max_length=255, default='Sin nombre')
    categoria = models.CharField(max_length=255, default='Sin categoría')
    subcategoria = models.CharField(max_length=255, default='Sin subcategoría')
    tamaño = models.CharField(max_length=255, default='Sin tamaño')
    color = models.CharField(max_length=255, default='Sin color')
    medidas = models.CharField(max_length=255, default='Sin medidas')
    marca = models.CharField(max_length=255, default='Sin marca')
    modelo = models.CharField(max_length=255, default='Sin modelo')
    descripcion = models.TextField(default='Sin descripción')
    stock = models.IntegerField(default=0)
    fecha = models.DateField(default=timezone.now)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    envio = models.BooleanField(default=False)
    tiempo_entrega = models.IntegerField(choices=[(8, '8 horas'), (12, '12 horas'), (24, '24 horas'), (48, '48 horas')], default=24)
    garantia = models.BooleanField(default=False)
    servicio_tecnico = models.BooleanField(default=False)
    imagen1 = models.ImageField(upload_to='productos/', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='productos/', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='productos/', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
