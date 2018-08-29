from flask import Flask, make_response
from .launcher import connect_to_api
from .tools import protect_request


TOKEN = None
app = Flask(__name__)


@app.route('/ping')
@protect_request
def ping():
    return make_response('', 204)


def launch():
    global TOKEN

    TOKEN = connect_to_api()
    app.run(host='0.0.0.0', port=8887)
