from rest_framework_json_api import serializers

from inmobiliaria.serializers import InmobiliariaSerializer
from inmueble.models import Casa, Servicio


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('nombre', 'fecha_creacion', 'usuario')

    included_serializers = {
        'usuario': 'usuario.serializers.UsuarioSerializer',
    }

    def validate_nombre(self, value):
        # Validamos por nombre
        if value.startswith('cancha'):
            raise serializers.ValidationError('El nombre no puede comenzar con cancha')


class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = serializers.ALL_FIELDS

    included_serializers = {
        'inmobiliaria': InmobiliariaSerializer,
        'servicios': ServicioSerializer,
    }
