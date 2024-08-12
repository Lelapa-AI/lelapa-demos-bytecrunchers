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

    result = requests.post(url, headers=headers, json=data)
}
