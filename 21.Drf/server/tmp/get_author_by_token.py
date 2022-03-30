import requests


#{'token': 'd66b4c73171219c55f4c0243ae06a3625fd02d8c'}
headers={'Authorization':"Token d66b4c73171219c55f4c0243ae06a3625fd02d8c"}
response = requests.get('http://127.0.0.1:8000/api/creators/', headers=headers)

print(response.status_code)
print(response.json())