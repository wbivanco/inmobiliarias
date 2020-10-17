from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet

from inmobiliaria.filters import InmobiliariaFilter
from inmobiliaria.models import Inmobiliaria
from inmobiliaria.serializers import InmobiliariaSerializer


class InmobiliariaViewSet(ReadOnlyModelViewSet):
    queryset = Inmobiliaria.objects.all()
    serializer_class = InmobiliariaSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_class = InmobiliariaFilter
