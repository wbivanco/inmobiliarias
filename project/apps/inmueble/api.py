from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from inmueble.filters import ServicioFilter
from inmueble.models import Casa, Servicio
from inmueble.serializers import CasaSerializer, ServicioSerializer


class ServicioViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    """
    Una ViewSet se documenta con las triples comillas, sean dobles (") o simples (')
    """
    queryset = Servicio.objects.activos().order_by('-nombre')
    serializer_class = ServicioSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, )
    filter_class = ServicioFilter
<<<<<<< HEAD

=======
>>>>>>> 58e412652a88c2d69806aa6c9bf71bf57c642431

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class CasaViewSet(ReadOnlyModelViewSet):
    """
    Endpoint para retornar todas las casas
    """
    queryset = Casa.objects.activos().select_related(
        'inmobiliaria',
        'usuario'
    ).prefetch_related(
        Prefetch('servicios', queryset=Servicio.objects.select_related('usuario'))
    ).order_by('nombre')

    serializer_class = CasaSerializer
