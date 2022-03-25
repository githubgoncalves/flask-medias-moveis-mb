import pytest
import mock
from api.app import app


TARGET_ADAPTER_REQUEST = (
    "api.main.adapter.flask_adapter"
)

def _adapter_request(*args):
    response = ["status_code"]
    response.status_code = 200
    return response

@pytest.fixture
def api():
    app.config['TESTING'] = True
    api = app.test_client()
    yield api

@mock.patch(TARGET_ADAPTER_REQUEST, side_effect=_adapter_request)
def test_find_mms(api, *args):
    json = {
        "range": 20,
        "from": 1647898546,
        "to": 1647898546
    }
    retorno = api.get("/v1/indicators/BRLBTC/mms", json=json)
    assert retorno.get_json()