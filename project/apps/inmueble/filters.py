from django_filters import rest_framework as filters

from inmueble.models import Servicio


class ServicioFilter(filters.FilterSet):
    class Meta:
        model = Servicio
        fields = ('buscar', )

    buscar = filters.CharFilter(field_name='nombre', lookup_expr='icontains')
