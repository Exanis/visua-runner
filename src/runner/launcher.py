from os import getenv
import requests


def connect_to_api():
    target_server = getenv('API_SERVER')
    target_token = getenv('API_TOKEN')
    runner_addr = getenv('RUNNER_ADDR')
    runner_name = getenv('RUNNER_NAME', runner_addr)
    result = requests.post(target_server, {
        'token': target_token,
        'name': runner_name,
        'addr': runner_addr
    })
    if result.status_code != 201:
        raise Exception("Invalid response from the api: " + result.text)
    data = result.json()
    return data['key']
