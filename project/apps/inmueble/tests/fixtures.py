import pytest
from decimal import Decimal

from inmobiliaria.tests.fixtures import crear_inmobiliaria
from inmueble.models import Casa, Servicio


def crear_servicio(nombre):
    servicio, _ = Servicio.objects.get_or_create(nombre=nombre)
    return servicio


@pytest.fixture
def crear_servicios():
    gas = crear_servicio(nombre='Gas')
    pileta = crear_servicio(nombre='Pileta')
    asador = crear_servicio(nombre='Asador')

    return gas, pileta, asador


@pytest.fixture
def crear_casas(crear_servicios):
    gas, pileta, asador = crear_servicios

    casa_1, _ = Casa.objects.get_or_create(
        nombre='Casa con Patio',
        medidas='30x25',
        moneda=Casa.DOLAR,
        precio=Decimal(50000),
        en_venta=True,
        en_alquiler=False,
        inmobiliaria=crear_inmobiliaria(nombre='Ambato'),
        metros_cubiertos=50,
        cantidad_habitaciones=4,
        cantidad_banios=3,
        cantidad_suite=1
    )

    casa_1.servicios.add(gas, pileta)

    casa_2, _ = Casa.objects.get_or_create(
        nombre='Casa con Pileta',
        medidas='30x25',
        moneda=Casa.PESO,
        precio=Decimal(300000),
        en_venta=True,
        en_alquiler=False,
        inmobiliaria=crear_inmobiliaria(nombre='Lira'),
        metros_cubiertos=50,
        cantidad_habitaciones=4,
        cantidad_banios=3,
        cantidad_suite=1
    )

    casa_2.servicios.add(gas, asador)

    casa_3, _ = Casa.objects.get_or_create(
        nombre='Chalet familiar',
        medidas='30x25',
        moneda=Casa.EURO,
        precio=Decimal(300),
        en_venta=False,
        en_alquiler=True,
        inmobiliaria=crear_inmobiliaria(nombre='Guerrero'),
        metros_cubiertos=50,
        cantidad_habitaciones=3,
        cantidad_banios=2,
        cantidad_suite=0
    )

    casa_3.servicios.add(gas)

    return casa_1, casa_2, casa_3
