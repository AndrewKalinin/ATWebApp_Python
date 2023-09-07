import requests
import yaml
import logging

with open("testdata.yaml", "r") as f:
	d = yaml.safe_load(f)


def auth():
	data = {
		"username": d["login"],
		"password": d["password"]
	}
	res = requests.post(url=d["url_auth"], data=data)
	if res:
		logging.debug("API: Received data from the server during authorization")
		return res.status_code
	else:
		logging.error("API: Data was not received from the server during authorization")
		return None


def post(title, description, content):
	headers = {
		'X-Auth-Token': d["token"]
	}
	data = {
		"title": title,
		"description": description,
		"content": content,
	}
	try:
		res = requests.post(url=d["url_post"], headers=headers, json=data)
		logging.debug("API: Send data for creating a post")
		return res.json()["description"]
	except:
		logging.exception("API: Data was not received from the server when creating a post")
		return None


if __name__ == '__main__':
	print(auth())
	print(post("aa", "sss", "fff"))
