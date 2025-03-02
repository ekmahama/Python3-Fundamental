# url = api.open-notify.org/astros.json
# python -m venv venv
# source venv/bin/activate
# pip install requests
# python space.py

import requests

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
for p in data["people"]:
    print(f"{p['name']} is on the {p['craft']} craft.")
