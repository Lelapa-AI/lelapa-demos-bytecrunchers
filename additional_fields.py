'''this module adds additional fields to the whatsapp user profile and is used upon user onboarding'''
from config import API_TOKEN as token
import requests

url = "https://whatsapp.turn.io/v1/contacts/schemas"

headers = {
    'Authorization': token, 
    'Accept':'application/vnd.v1+json', 
    'Content-Type':'application/json'
}

def add_field(name, display, t, default, is_private=True):
    data = {
    'version':'0.0.1-alpha', 
    'fields':[{
            "name": name,
            "display": display,
            "type": t,
            "default": default,
            "is_private": is_private
    }]
    }

    result = requests.post(url, headers=headers, json=data)



#  curl -X POST https://whatsapp.turn.io/v1/contacts/schemas \
#     -H 'Authorization: Bearer token' \
#     -H 'Accept: application/vnd.v1+json' \
#     -H 'Content-Type: application/json' \
#     -d '{
#         "version": "0.0.1-alpha",
#         "fields": [{
#             "name": "consent",
#             "display": "Consent Given",
#             "type": "BOOLEAN",
#             "default": false,
#             "is_private": true
#         }, {
#             "name": "gender",
#             "display": "Gender",
#             "type": "ENUM",
#             "null": false,
#             "is_private": false,
#             "default": "UNDISCLOSED",
#             "enum": [
#                 {"value": "MALE", "display": "Male"},
#                 {"value": "FEMALE", "display": "Female"},
#                 {"value": "OTHER", "display": "Other"},
#                 {"value": "UNDISCLOSED", "display": "Undisclosed"}
#             ]
#         }]
#     }'


def create_consent_field():
    data = {"version":"0.0.1-alpha", "fields":[{
            "name":"latest_user_question", 
            "display":"Latest question", 
            "type":"STRING",
            "default":"None",
            "null":True,
            "is_private": True
        }, 
        {
            "name":"lang", 
            "display":"Language", 
            "type":"STRING",
            "default":"None",
            "null":True,
            "is_private": True
        }, 
        {
            "name":"nearest_clinic", 
            "display":"HealthSpot", 
            "type":"STRING",
            "default":"None",
            "null":True,
            "is_private": True
        }
        
        ]}

    # data = {"version":"0.0.1-alpha", "fields":[{
    #     "name":"latest_user_question", 
    #     "display":"Latest question", 
    #     "type":"STRING",
    #     "default":"None",
    #     "is_private": True
    # }]}
    
    
    res = requests.post(url, headers=headers, json=data)
    return res





