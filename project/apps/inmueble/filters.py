from django_filters import rest_framework as filters

from inmueble.models import Servicio, Casa


class ServicioFilter(filters.FilterSet):
    class Meta:
        model = Servicio
        fields = ('buscar', )

    buscar = filters.CharFilter(field_name='nombre', lookup_expr='icontains', label='Nombre')


class CasaFilter(filters.FilterSet):
    class Meta:
        model = Casa
        fields = ('nombre', 'en_alquiler', 'en_venta', 'precio')

    nombre = filters.CharFilter(field_name='nombre', lookup_expr='icontains', label='Nombre')
    precio = filters.RangeFilter()
