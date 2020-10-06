from rest_framework import routers

from inmobiliaria import api as api_inmobiliaria
from inmueble import api as api_inmueble

router = routers.DefaultRouter()

router.register(prefix='inmobiliaria', viewset=api_inmobiliaria.InmobiliariaViewSet)
router.register(prefix='casa', viewset=api_inmueble.CasaViewSet)
router.register(prefix='servicio', viewset=api_inmueble.ServicioViewSet)
