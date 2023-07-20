import requests
import json
import util


def add_item(username: str, item):
    data = {
        "username": username,
        "item": {
            "name": item['name'],
            "description": item['description']
        }
    }

    try:
        response = requests.post("http://127.0.0.1:5000/inventory/add", json=data)
    except:
        return None
    
    if response.status_code == 200:
        return response.json()
    else:
        return None



def create(username: str):
    data = {
        "username": username
    }

    try:
        response = requests.post("http://127.0.0.1:5000/create", json=data)
    except:
        return None


    if response.status_code == 200:
        login(username)
    else:
        return None


def login(username: str):
    data = {
        "username": username
    }

    try:
        response = requests.post("http://127.0.0.1:5000/login", json=data)
    except:
        return

    if response.status_code == 200:
        if response.json()['inventory'] != '':
            inventory = json.loads(response.json()['inventory'])
        else:
            inventory = []

        user = util.User(username, inventory)

        return user
    else:
        return None