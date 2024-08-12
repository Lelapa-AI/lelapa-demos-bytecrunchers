import requests
from config import API_TOKEN as token

url = "https://whatsapp.turn.io/v1/messages"
headers = {"Authorization": token, "Content-Type":"application/json"}

def send_message():
        data = {"preview_url": False | True, 
        "recepient_type":"individual", 
        "from":"27671401556",
        "type":"text"
        }

        res = requests.post(url, headers=headers, json=data)
        return res.json()