from rest_framework.viewsets import ReadOnlyModelViewSet

from inmobiliaria.models import Inmobiliaria
from inmobiliaria.serializers import InmobiliariaSerializer


class InmobiliariaViewSet(ReadOnlyModelViewSet):
    queryset = Inmobiliaria.objects.all()
    serializer_class = InmobiliariaSerializer
