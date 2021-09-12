import requests

response = requests.post('http://127.0.0.1:8000/api-token/', data={'username': 'django', 'password': 'geekbrains'})
# print(response.json())
#{'token': '16cdc4e104844ecee4451961b24bbf64c95b75b4'}
payload= {'username': 'django', 'password': 'geekbrains'}
