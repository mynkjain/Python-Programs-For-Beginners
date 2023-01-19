import requests;
response = requests.get("http://api.open-notify.org/astros.json")
response_json = response.json()

for person in response_json["people"]:
    print(person["name"])
