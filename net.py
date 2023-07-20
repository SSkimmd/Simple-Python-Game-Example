import requests
import json
import util


def add_item(username: str):
    pass


def login(username: str):
    data = {
        "username": username
    }

    response = requests.post("http://127.0.0.1:5000/login", json=data)

    if response.status_code == 200:
        inventory = json.loads(response.json()['inventory'])

        user = util.User(username, inventory)

        return user
    else:
        return None