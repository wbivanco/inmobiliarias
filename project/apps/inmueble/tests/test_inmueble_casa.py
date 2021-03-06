import pytest

from core.tests.utils import get
from inmobiliaria.models import Inmobiliaria
from inmueble.tests.fixtures import crear_casas, crear_servicios


@pytest.mark.django_db
def test_obtener_casas_activas_con_data_de_servicios_e_inmobiliaria(crear_casas, crear_servicios):
    casa_1, casa_2, casa_3 = crear_casas
    casa_2.desactivar()

    inmobiliaria_guerrero = Inmobiliaria.objects.get(nombre='Guerrero')
    inmobiliaria_ambato = Inmobiliaria.objects.get(nombre='Ambato')

    endpoint = "/api/v1/casa/?include=servicios,inmobiliaria"
    response = get(endpoint)
    assert response.status_code == 200

    json_data = response.json()
    data = json_data['data']
    meta = json_data['meta']

    assert 'included' in json_data
    included = json_data['included']

    assert meta['pagination']['count'] == 2

    assert data[0]['type'] == 'Casa'
    assert data[0]['attributes']['nombre'] == 'Casa con Patio'
    assert len(data[0]['relationships']['servicios']['data']) == 2
    assert data[0]['relationships']['inmobiliaria']['data']['type'] == 'Inmobiliaria'
    assert data[0]['relationships']['inmobiliaria']['data']['id'] == str(inmobiliaria_ambato.id)

    assert data[1]['type'] == 'Casa'
    assert data[1]['attributes']['nombre'] == 'Chalet familiar'
    assert len(data[1]['relationships']['servicios']['data']) == 1
    assert data[1]['relationships']['inmobiliaria']['data']['type'] == 'Inmobiliaria'
    assert data[1]['relationships']['inmobiliaria']['data']['id'] == str(inmobiliaria_guerrero.id)

    assert len(included) == 4
