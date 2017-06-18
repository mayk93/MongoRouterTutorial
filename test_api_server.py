import requests

print(requests.get("http://localhost:8000/data").text)
print(requests.post("http://localhost:8000/data", {"name": "John Smith", "value": 5}).text)