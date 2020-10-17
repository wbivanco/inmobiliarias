from django_filters import rest_framework as filters

from inmobiliaria.models import Inmobiliaria


class InmobiliariaFilter(filters.FilterSet):
    class Meta:
        model = Inmobiliaria
        fields = ('nombre', 'email')
