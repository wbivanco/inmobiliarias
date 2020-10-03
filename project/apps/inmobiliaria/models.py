from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from core.models import ModeloBase


class Inmobiliaria(ModeloBase):
    class Meta:
        verbose_name = 'Inmobiliaria'
        verbose_name_plural = 'Inmobiliarias'

    nombre = models.CharField(max_length=90)
    direccion = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    codigo_postal = models.CharField(max_length=15)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=50, default="Catamarca")
    pais = models.CharField(max_length=50, default="Argentina")
    slogan = models.CharField(max_length=200, blank=True)
    horario_atencion = models.TextField(blank=True)

    # Relaciones Genéricas.
    telefonos = GenericRelation('util.Telefono')
    redes_sociales = GenericRelation('util.RedSocial')

    def __str__(self):
        return self.nombre
