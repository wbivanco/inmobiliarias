from django_filters import rest_framework as filters

from inmueble.models import Servicio


class InmuebleFilter(filters.FilterSet):
    class Meta:
        model = Servicio
        fields = ('nombre', )
