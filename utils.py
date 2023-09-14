import json
import requests


def get_data_from_json_file():
    with open('data/link.json') as f:
        return json.load(f)

def get_questions_data_by_requests():
    request_url = get_data_from_json_file()['eq']
    response = requests.get(request_url)
    return response.json()