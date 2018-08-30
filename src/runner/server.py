import logging
from flask import Flask, make_response, request, abort
from .launcher import connect_to_api


TOKEN = None
APP = Flask(__name__)
LOGGER = logging.getLogger(__name__)


def _authenticate_request():
    if TOKEN != request.headers.get('X-Auth-Token', ''):
        LOGGER.error('Invalid request received (bad or no auth token)')
        return False
    return True


def protect_request(func):
    def wrapper():  # pylint: disable=inconsistent-return-statements
        if _authenticate_request():
            response = func()
            response.headers['X-Auth-Token'] = TOKEN
            return response
        abort(401)
    return wrapper


@APP.route('/ping')
@protect_request
def ping():
    return make_response('', 204)


def launch():
    global TOKEN  # pylint: disable=global-statement

    TOKEN = connect_to_api()
