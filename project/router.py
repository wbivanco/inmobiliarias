from rest_framework import routers

from inmobiliaria import api as api_inmobiliaria


router = routers.DefaultRouter()

router.register(prefix='inmobiliaria', viewset=api_inmobiliaria.InmobiliariaViewSet)
