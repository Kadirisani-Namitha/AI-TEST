import requests

url = "http://127.0.0.1:8000/process"
data = {"prompt": "Create a robot with wings"}

response = requests.post(url, json=data)
print(response.json())
