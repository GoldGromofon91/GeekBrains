import requests


#{'token': 'd66b4c73171219c55f4c0243ae06a3625fd02d8c'}
headers={'Authorization':"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMDUyODY5LCJqdGkiOiJjNzRmOTFhZTVjZGQ0OTVlYTkwMTRiN2NhZDgwNmMzNSIsInVzZXJfaWQiOjF9.IsJ4WQPrK0jeZjkU6ssATbxAhTCu8fVB016tB2Nyl3U"}
response = requests.get('http://127.0.0.1:8000/api/creators/', headers=headers)

print(response.status_code)
print(response.json())