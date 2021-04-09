import json

obj={}
with open ('secret.json','r') as file:
    obj = json.load(file)

key = obj.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY','')
secret = obj.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET','')

print(key,secret)