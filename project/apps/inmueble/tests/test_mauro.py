import pytest

from core.tests.utils import get, post
from inmueble.tests.fixtures import crear_servicios
from inmueble.tests.fixtures import crear_casas, crear_servicios
from usuario.tests.fixtures import crear_usuario

@pytest.mark.django_db
def test_listado_inmueble_filtrar_en_venta(crear_casas, crear_servicios):
    casa_1, casa_2, casa_3 = crear_casas
    usuario_autenticado = crear_usuario('debianitram')

    response = get('/api/v1/casa/?en_venta=true', user_logged=usuario_autenticado)
    assert response.status_code == 200
    json_data = response.json()
    data = json_data['data']
    meta = json_data['meta']

    assert meta['pagination']['count'] == 2


@pytest.mark.django_db
def test_listado_inmueble_filtrar_en_alquiler(crear_casas, crear_servicios):
    casa_1, casa_2, casa_3 = crear_casas
    usuario_autenticado = crear_usuario('debianitram')

    response = get('/api/v1/casa/?en_alquiler=true', user_logged=usuario_autenticado)
    assert response.status_code == 200
    json_data = response.json()
    data = json_data['data']
    meta = json_data['meta']

    assert meta['pagination']['count'] == 1