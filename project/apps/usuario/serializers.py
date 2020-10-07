from django.contrib.auth import get_user_model
from rest_framework_json_api import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name')
