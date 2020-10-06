from rest_framework import serializers

from inmobiliaria.serializers import InmobiliariaSerializer
from inmueble.models import Casa, Servicio


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = serializers.ALL_FIELDS

    def validate_nombre(self, value):
        if value.startswith('cancha'):
            raise serializers.ValidationError('El nombre no puede comenzar con cancha')

        return value


class CasaSerializer(serializers.ModelSerializer):
    servicios = serializers.StringRelatedField(many=True)
    inmobiliaria = InmobiliariaSerializer()

    class Meta:
        model = Casa
        fields = serializers.ALL_FIELDS
