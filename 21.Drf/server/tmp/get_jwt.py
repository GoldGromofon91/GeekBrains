import requests


payload= {'username': 'django', 'password': 'geekbrains'}
response = requests.post('http://127.0.0.1:8000/api/token/jwt/', data=payload)
print(response.json())
#{'refresh': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMTcyNjE0MiwianRpIjoiOWM4YzMwZTA3MTVkNDM2ZGEwNDEyNWUyOGFjZjU3NjEiLCJ1c2VyX2lkIjoxMX0.IqX3R2jWmjk0KH8kSSfw_yXjmPvqw9fb9QF2bK0C4Ow'}
# {'access': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMxNjQwMDQyLCJqdGkiOiI3OTM5ZWQ2MDBjMWQ0MDU2OTk2YjcxMzRkYzE5Y2FkNSIsInVzZXJfaWQiOjExfQ.ZLiJD4LQM7I4Xrgbfd9eDbsTIvrh_KCuP2ZHF_kcrJM'}
