from django.db.models import Prefetch
from rest_framework import mixins
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from inmueble.models import Casa, Servicio
from inmueble.serializers import CasaSerializer, ServicioSerializer


class ServicioViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    """
    Una ViewSet se documenta con las triples comillas, sean dobles (") o simples (')
    """
    queryset = Servicio.objects.activos()
    serializer_class = ServicioSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class CasaViewSet(ReadOnlyModelViewSet):
    """
    Endpoint para retornar todas las casas
    """
    queryset = Casa.objects.all().select_related(
        'inmobiliaria',
        'usuario'
    ).prefetch_related(
        Prefetch('servicios', queryset=Servicio.objects.select_related('usuario'))
    )

    serializer_class = CasaSerializer
