import pytest
from unittest import mock
from runner.launcher import connect_to_api


class FakeRequestResult(object):
    status_code = 201
    text = 'error'

    def json(self):
        return {
            'key': 'test'
        }


@mock.patch('requests.post')
@mock.patch('runner.launcher.getenv')
def test_launch_register(getenv_mock, post_mock):
    getenv_mock.return_value = 'testing'
    post_mock.return_value = FakeRequestResult()
    key = connect_to_api()
    post_mock.assert_called_once_with('testing', {
        'token': 'testing',
        'name': 'testing',
        'addr': 'testing'
    })
    assert key == 'test'


@mock.patch('requests.post')
@mock.patch('runner.launcher.getenv')
def test_launch_register_error(getenv_mock, post_mock):
    getenv_mock.return_value = 'testing'
    post_mock.return_value = FakeRequestResult()
    post_mock.return_value.status_code = 400
    with pytest.raises(Exception):
        connect_to_api()
