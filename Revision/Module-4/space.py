# url = api.open-notify.org/astros.json
import requests


data = requests.get('http://api.open-notify.org/astros.json')
json = data.json()

peoples = json['people']

for person in peoples:
    print(f"Name : {person['name']}, craft: {person['craft']}")
