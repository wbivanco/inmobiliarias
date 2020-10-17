from django_filters import rest_framework as filters

from inmueble.models import Servicio


class ServicioFilter(filters.FilterSet):
    class Meta:
        model = Servicio
        fields = ('nombre', )
