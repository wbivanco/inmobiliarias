from rest_framework_json_api import serializers

from inmobiliaria.serializers import InmobiliariaSerializer
from inmueble.constants import LISTA_NOMBRE_NO_PERMITIDOS
from inmueble.models import Casa, Servicio


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('nombre', 'fecha_creacion', 'usuario')

    included_serializers = {
        'usuario': 'usuario.serializers.UsuarioSerializer',
    }

    def validate_nombre(self, nombre):
        nombre = nombre.lower()
        if Servicio.objects.activos().filter(nombre=nombre).exists():
            raise serializers.ValidationError('El servicio {} ya existe'.format(nombre))

        if nombre.startswith(LISTA_NOMBRE_NO_PERMITIDOS):
            raise serializers.ValidationError('El nombre indicado comienza con un valor no permitido')

        return nombre


class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = serializers.ALL_FIELDS

    included_serializers = {
        'inmobiliaria': InmobiliariaSerializer,
        'servicios': ServicioSerializer,
    }
