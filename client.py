import requests
response = requests.get("http://127.0.0.1:8000/add", params={"a": 3, "b": 4})
print(response.json())