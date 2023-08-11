import requests
import yaml

with open("config.yaml", "r") as f:
    d = yaml.safe_load(f)

def auth_admin():
    data = {
        'username': d["username"],
        'password': d["password"],
    }
    res = requests.post(url=d["url_auth"], data=data)
    return res.json()["token"]

def auth_user():
    headers = {
        'Authorization': f'Bearer{d["X-Auth-Token"]}'
    }
    data = {
        'username': d["username1"],
        'password': d["password1"],
    }
    res = requests.post(url=d["url_auth"], data=data, headers=headers)
    return res.status_code

def posts_another_user():
    headers = {
        'X-Auth-Token': d["user_token"],
    }
    data = {
        'username': d["username1"],
        'owner': d['owner'],
    }
    res = requests.get(url=d["url_post"], data=data, headers=headers)
    return res.status_code

def create_post():
    headers = {
        'X-Auth-Token': d["user_token"],
    }
    data = {
        'username': d["username1"],
        'title': d['title'],
        'description': d['description'],
        'content': d['content'],
    }
    res = requests.post(url=d["url_create_post"], data=data, headers=headers)
    return res.json()['description']

if __name__ == '__main__':
    print(create_post())