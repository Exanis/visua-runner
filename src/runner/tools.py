import logging
from flask import request, abort
from .server import TOKEN


logger = logging.getLogger(__name__)


def _authenticate_request():
    if TOKEN != request.headers.get('X-Auth-Token', ''):
        logger.error('Invalid request received (bad or no auth token)')
        return False
    return True


def protect_request(func):
    def wrapper():
        if _authenticate_request():
            response = func()
            response.headers['X-Auth-Token'] = TOKEN
            return response
        abort(401)
    return wrapper
