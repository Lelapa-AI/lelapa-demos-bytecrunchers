import requests
from config import API_TOKEN as token

headers = {"Authorization": token,
            "Accept":"application/vnd.v1+json",
            "Content-Type":"apllication/json"
            }

# curl -X PATCH https://whatsapp.turn.io/v1/contacts/27123456789/profile \
#     -H 'Authorization: Bearer token' \
#     -H 'Accept: application/vnd.v1+json' \
#     -H 'Content-Type: application/json' \
#     -d '{"name": "Fizbo"}'



# name: STRING, allowed to be null
# surname: STRING, allowed to be null
# location: LOCATION, allowed to be null
# language: ENUM, limited to ISO-639-3 country codes, allowed to be null
# opted_in: BOOLEAN, defaults to false
# opted_in_at: DATETIME, allowed to be null
# birthday: DATETIME, allowed to be null
# whatsapp_profile_name: STRING, allowed to be null
# whatsapp_id: STRING, allowed to be null

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJUdXJuIiwiZXhwIjoxNzIzOTAzMDcyLCJpYXQiOjE3MjMyOTgyNzIsImlzcyI6IlR1cm4iLCJqdGkiOiJiYmZiZDIxYy1hMTRmLTQwNjktOGY4Zi0yZGZhN2RkNWM0N2EiLCJuYmYiOjE3MjMyOTgyNzEsInN1YiI6Im51bWJlcjo1OTk0IiwidHlwIjoiYWNjZXNzIn0.hAZXHYuGivuJSt8dTtJ_fbcIYER7vzsi1j8U_1BF0g4EAAfHCIoYi6hGyVwWeH3SvtmnWmhTAHfblEM-O5qNkw', 
    'Accept':'application/vnd.v1+json', 
    'Content-Type':'application/json'}



    
# url = f"https://whatsapp.turn.io/v1/contacts/{str(contact_number)}/profile"

# data = {'name': name}

# # data = {'name': 'Fibzo', 
# #         'surname':'',
# #         'location':'', 
# #         'language':'', 
# #         'birthday':'';
# #         'whatsapp_profile_name':''
# # }
# res = requests.patch(url, headers=headers, json=data)
# print(res.json())

# TODO: code function to convert language to ISO-639-3 country codes
# TODO: function to convert boolean values for consent from y/n to true/false
# TODO: create location object with keys lat & long


def update_whatsapp_profile_info(user):
    url = f"https://whatsapp.turn.io/v1/contacts/{user.w_id}/profile"
    data = {
        "name":user.f_name, 
        "surname":user.s_name, 
        "language": None, 
        "location":None, 
        "consent":True, 
    }

    res = requests.patch(url, headers=headers, json=data)
    print(res.json().get('schema'))
    return res.json().get('schema')




# $ curl -X PATCH https://whatsapp.turn.io/v1/contacts/27123456789/profile \
#     -H 'Authorization: Bearer token' \
#     -H 'Accept: application/vnd.v1+json' \
#     -H 'Content-Type: application/json' \
#     -d '{"name": "Fizbo"}'
# > '{
#     "version": "0.0.1-alpha",
#     "generation": 2,
#     "schema": "<the-schema-uuid>",
#     "fields": {
#         "language": "ENG",
#         "date_of_birth": null,
#         "age": 2,
#         "consent": false,
#         "location": null,
#         "name": "Fizbo",
#         "risk_profile": 2.0,
#         "surname": null,
#         "birthday": null,
#         "opted_in": false,
#         "opted_in_at": null,
#         "whatsapp_id": null,
#         "whatsapp_profile_name": null
#     }
# }'