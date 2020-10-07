from rest_framework_json_api import serializers

from inmobiliaria.models import Inmobiliaria


class InmobiliariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmobiliaria
        fields = serializers.ALL_FIELDS
