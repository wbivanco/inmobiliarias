from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from inmueble.models import Casa, Servicio
from inmueble.serializers import CasaSerializer, ServicioSerializer


class ServicioViewSet(ModelViewSet):
    """
    Una ViewSet se documenta con las triples comillas, sean dobles (") o simples (')
    """
    queryset = Servicio.objects.activos()
    serializer_class = ServicioSerializer


class CasaViewSet(ReadOnlyModelViewSet):
    """
    Endpoint para retornar todas las casas
    """
    queryset = Casa.objects.all().prefetch_related('servicios').select_related('inmobiliaria')
    serializer_class = CasaSerializer
