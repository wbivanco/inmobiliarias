from django.db import models

from core.models import ModeloBase
from inmueble.querysets import ServicioQuerySet, InmuebleBaseQuerySet


class Servicio(ModeloBase):
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    nombre = models.CharField(max_length=50, unique=True)

    objects = ServicioQuerySet.as_manager()

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.nombre = self.nombre.lower()
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


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
    moneda = models.CharField(max_length=5, choices=MONEDAS, default=PESO)
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    descripcion = models.TextField(blank=True)
    en_venta = models.BooleanField(default=False)
    en_alquiler = models.BooleanField(default=False)

    # Relaciones
    servicios = models.ManyToManyField(Servicio, blank=True)

    inmobiliaria = models.ForeignKey(
        'inmobiliaria.Inmobiliaria',
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    objects = InmuebleBaseQuerySet.as_manager()

    def __str__(self):
        return self.nombre


class Casa(InmuebleBase):
    class Meta:
        verbose_name = 'Casa'
        verbose_name_plural = 'Casas'

    metros_cubiertos = models.IntegerField(verbose_name='Metros Cubiertos')
    cantidad_habitaciones = models.IntegerField(verbose_name='Cantidad de habitaciones')
    cantidad_banios = models.IntegerField(verbose_name='Cantidad de Baños')
    cantidad_suite = models.IntegerField(verbose_name='Cantidad de Suite')

    # TODO: Añadir los campos faltantes.
