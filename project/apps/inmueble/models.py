from django.conf import settings
from django.db import models

from project.apps.core.models import ModeloBase


class Servicio(ModeloBase):
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    nombre = models.CharField(max_length=50)


class InmuebleBase(ModeloBase):
    class Meta:
        verbose_name = 'Inmueble Base'
        abstract = True

    PESO = 'peso'
    DOLAR = 'dolar'
    EURO = 'euro'
    REAL = 'real'

    MONEDAS = [
        (PESO, 'Peso'),
        (DOLAR, 'Dólar'),
        (EURO, 'Euro'),
        (REAL, 'Real')
    ]

    nombre = models.CharField(max_length=80)
    medidas = models.CharField(max_length=30, blank=True)
    moneda = models.CharField(max_length=1, choices=MONEDAS, default=PESO)
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    descripcion = models.TextField(blank=True)
    en_venta = models.BooleanField(default=False)
    en_alquiler = models.BooleanField(default=False)

    # Relaciones
    servicios = models.ManyToManyField(Servicio)

    # Auditoria
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
