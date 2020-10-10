from inmobiliaria.models import Inmobiliaria


def crear_inmobiliaria(nombre):
    inmobiliaria, _ = Inmobiliaria.objects.get_or_create(
        nombre=nombre,
        direccion='Calle sin salida 123',
        codigo_postal='4707',
        localidad='San Fernando',
    )

    return inmobiliaria
