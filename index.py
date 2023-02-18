import requests

url = "https://randomuser.me/api/?results=100&inc=name,gender&gender=male"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error retrieving users fro API")
