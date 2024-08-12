import requests
from config import API_TOKEN as token

headers = {
    "Authorization": token,
    "Accept": "application/vnd.v1+json"
}

def get_user_profile(number):
    url = f"https://whatsapp.turn.io/v1/contacts/{number}/profile"
    response = requests.get(url, headers=headers)

    return response.json()



