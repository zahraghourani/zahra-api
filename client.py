import requests
url = "https://my-api.onrender.com/add"
params = {"a": 10, "b": 20}
r = requests.get(url, params=params)
print(r.json())