import requests

payload= {'username': 'django', 'password': 'geekbrains'}
response = requests.post('http://127.0.0.1:8000/api-token/', data=payload)
print(response.json())
#{'token': 'd66b4c73171219c55f4c0243ae06a3625fd02d8c'}

