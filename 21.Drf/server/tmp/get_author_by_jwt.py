import requests


#{'token': 'd66b4c73171219c55f4c0243ae06a3625fd02d8c'}
headers={'Authorization':"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMxNjQwMDQyLCJqdGkiOiI3OTM5ZWQ2MDBjMWQ0MDU2OTk2YjcxMzRkYzE5Y2FkNSIsInVzZXJfaWQiOjExfQ.ZLiJD4LQM7I4Xrgbfd9eDbsTIvrh_KCuP2ZHF_kcrJM"}
response = requests.get('http://127.0.0.1:8000/api/creators/', headers=headers)

print(response.status_code)
print(response.json())