import pytest
from unittest.mock import patch
from runner import server


@pytest.fixture
def client():
    server.APP.config['TESTING'] = True
    with patch('runner.server.connect_to_api') as mock_connect:
        mock_connect.return_value = 'test'
        server.launch()
    yield server.APP.test_client()


def test_ping_route(client):
    result = client.get('/ping', headers={'X-Auth-Token': 'test'})
    assert result.status_code == 204


def test_bad_auth(client):
    result = client.get('/ping')
    assert result.status_code == 401
    result = client.get('/ping', headers={'X-Auth-Token': 'bad_auth'})
    assert result.status_code == 401


@patch('runner.server.connect_to_api')
def test_get_app(mock_connect):
    mock_connect.return_value = 'test'
    server.get_app()
    mock_connect.assert_called_once()
    assert server.TOKEN == 'test'
