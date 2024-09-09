from config import API_TOKEN as token
import requests

url = "https://whatsapp.turn.io/v1/contacts/schemas"

headers = {
    'Authorization': token, 
    'Accept':'application/vnd.v1+json', 
    'Content-Type':'application/json'
}


def main():


    data = {"version":"0.0.1-alpha", "fields":[{
            "name":"latest_user_question", 
            "display":"Latest question", 
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


    res = requests.post(url, headers=headers, json=data)


    
    return res.text
    


def update_whatsapp_profile_info(user):
    url = f"https://whatsapp.turn.io/v1/contacts/{user}/profile"
    data = {
        "nearest_clinic":"Bara"
    }

    res = requests.patch(url, headers=headers, json=data)
    print(res.json().get('schema'))
    return res.json().get('schema')

    
    
    
    
    
if __name__ == "__main__":
    # print(main())
    print(update_whatsapp_profile_info("27671401556"))
