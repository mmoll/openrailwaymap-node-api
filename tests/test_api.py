import requests
from pytest import approx


API_BASE_URL = 'http://localhost:9003'


def test_get_facility_by_name():
    response = requests.get(f'{API_BASE_URL}/facility', params={'name': 'feldmoching'})

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    response_body = response.json()

    assert len(response_body) == 2

    assert response_body[0]['lat'] == approx(11.5410187)
    assert response_body[0]['lon'] == approx(48.213790699886196)
    assert response_body[0]['name'] == 'Feldmoching'
    assert response_body[0]['uicname'] is None
    assert response_body[0]['uicref'] is None
    assert response_body[0]['ref'] is None
    assert response_body[0]['id'] == '3189921161'
    assert response_body[0]['type'] == 'station'
    assert response_body[0]['operator'] is None
    assert response_body[0]['stationcategory'] is None

    assert response_body[1]['lat'] == approx(11.541275300000001)
    assert response_body[1]['lon'] == approx(48.213803599886198)
    assert response_body[1]['name'] == 'Feldmoching'
    assert response_body[1]['uicname'] is None
    assert response_body[1]['uicref'] == '8004147'
    assert response_body[1]['ref'] == 'MFE'
    assert response_body[1]['id'] == '2499552238'
    assert response_body[1]['type'] == 'station'
    assert response_body[1]['operator'] == 'DB Netz AG'
    assert response_body[1]['stationcategory'] is None


def test_get_facility_by_name_and_operator():
    response = requests.get(f'{API_BASE_URL}/facility', params={'name': 'feldmoching', 'operator': 'DB Netz AG'})

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    response_body = response.json()

    assert len(response_body) == 1

    assert response_body[0]['lat'] == approx(11.541275300000001)
    assert response_body[0]['lon'] == approx(48.213803599886198)
    assert response_body[0]['name'] == 'Feldmoching'
    assert response_body[0]['uicname'] is None
    assert response_body[0]['uicref'] == '8004147'
    assert response_body[0]['ref'] == 'MFE'
    assert response_body[0]['id'] == '2499552238'
    assert response_body[0]['type'] == 'station'
    assert response_body[0]['operator'] == 'DB Netz AG'
    assert response_body[0]['stationcategory'] is None


def test_get_facility_by_name_with_spaces():
    response = requests.get(f'{API_BASE_URL}/facility', params={'name': 'fischbach nürnberg'})

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    response_body = response.json()

    assert len(response_body) == 1

    assert response_body[0]['lat'] == approx(11.1743995)
    assert response_body[0]['lon'] == approx(49.4130807995908)
    assert response_body[0]['name'] == 'Fischbach (bei Nürnberg)'
    assert response_body[0]['uicname'] is None
    assert response_body[0]['uicref'] is None
    assert response_body[0]['ref'] == 'NFIH'
    assert response_body[0]['id'] == '1367866577'
    assert response_body[0]['type'] == 'station'
    assert response_body[0]['operator'] == 'DB Station&Service AG'
    assert response_body[0]['stationcategory'] is None


def test_get_facility_by_ref():
    response = requests.get(f'{API_BASE_URL}/facility', params={'ref':'mhrk'})

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    response_body = response.json()

    assert len(response_body) == 1

    assert response_body[0]['lat'] == approx(11.5096112)
    assert response_body[0]['lon'] == approx(48.043303899927402)
    assert response_body[0]['name'] == 'Höllriegelskreuth'
    assert response_body[0]['uicname'] is None
    assert response_body[0]['uicref'] == '8002899'
    assert response_body[0]['ref'] == 'MHRK'
    assert response_body[0]['id'] == '2514399802'
    assert response_body[0]['type'] == 'station'
    assert response_body[0]['operator'] == 'DB Netz AG'
    assert response_body[0]['stationcategory'] == '6'


def test_get_facility_by_uicref():
    response = requests.get(f'{API_BASE_URL}/facility', params={'uicref': '8000284'})

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    response_body = response.json()

    assert len(response_body) == 1

    assert response_body[0]['lat'] == approx(11.0823089)
    assert response_body[0]['lon'] == approx(49.445199099583)
    assert response_body[0]['name'] == 'Nürnberg Hauptbahnhof'
    assert response_body[0]['uicname'] is None
    assert response_body[0]['uicref'] == '8000284'
    assert response_body[0]['ref'] == 'NN'
    assert response_body[0]['id'] == '4543919208'
    assert response_body[0]['type'] == 'station'
    assert response_body[0]['operator'] == 'DB Station&Service AG'
    assert response_body[0]['stationcategory'] == '1'


def test_get_networklength():
    response = requests.get(f'{API_BASE_URL}/networklength')

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    response_body = response.json()

    found_element = {}
    for element in response_body:
        if element['operator'] == 'Ilztalbahn GmbH' and element['length'] == 70:
            found_element = element

    assert found_element == {'operator': 'Ilztalbahn GmbH', 'length': 70}
