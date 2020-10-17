import pytest

from core.tests.utils import get, post
from inmueble.tests.fixtures import crear_servicios
from usuario.tests.fixtures import crear_usuario


@pytest.mark.django_db
def test_falla_al_listar_servicios_sin_usuario_autenticado(crear_servicios):
    endpoint = '/api/v1/servicio/'
    response = get(endpoint)
    assert response.status_code == 403


@pytest.mark.django_db
def test_obtener_listado_servicios_activos_ordenados_nombre_descendente(crear_servicios):
    gas, pileta, asador = crear_servicios
    pileta.desactivar()

    usuario_autenticado = crear_usuario(username='debianitram')

    endpoint = '/api/v1/servicio/'
    response = get(endpoint, user_logged=usuario_autenticado)
    assert response.status_code == 200

    json_data = response.json()
    data = json_data['data']
    meta = json_data['meta']

    assert meta['pagination']['count'] == 2
    assert data[0]['type'] == 'Servicio'
    assert data[0]['attributes']['nombre'] == 'gas'

    assert data[1]['type'] == 'Servicio'
    assert data[1]['attributes']['nombre'] == 'asador'


@pytest.mark.django_db
def test_creacion_servicio():
    endpoint = '/api/v1/servicio/'
    usuario_autenticado = crear_usuario('debianitram')

    data = {
        "data": {
            "type": "Servicio",
            "attributes": {
                "nombre": "INTERNET"
            }
        }
    }

    response = post(endpoint, data=data, user_logged=usuario_autenticado)
    assert response.status_code == 201

    data_json = response.json()['data']
    assert data_json['type'] == 'Servicio'
    assert data_json['attributes']['nombre'] == 'internet'
    assert data_json['relationships']['usuario']['data']['type'] == 'User'
    assert data_json['relationships']['usuario']['data']['id'] == str(usuario_autenticado.id)


@pytest.mark.django_db
def test_creacion_servicio_falla_por_servicio_repetido(crear_servicios):
    endpoint = '/api/v1/servicio/'
    usuario_autenticado = crear_usuario('debianitram')

    data = {
        "data": {
            "type": "Servicio",
            "attributes": {
                "nombre": "Gas"
            }
        }
    }

    response = post(endpoint, data=data, user_logged=usuario_autenticado)
    assert response.status_code == 400
    errors = response.json()['errors']
    assert errors[0]['detail'] == 'El servicio gas ya existe'


@pytest.mark.django_db
def test_creacion_servicio_falla_por_nombre_de_servicio_no_permitidos(crear_servicios):
    endpoint = '/api/v1/servicio/'
    usuario_autenticado = crear_usuario('debianitram')

    data = {
        "data": {
            "type": "Servicio",
            "attributes": {
                "nombre": "Otro servicio"
            }
        }
    }

    response = post(endpoint, data=data, user_logged=usuario_autenticado)
    assert response.status_code == 400
    errors = response.json()['errors']
    assert errors[0]['detail'] == 'El nombre indicado comienza con un valor no permitido'


