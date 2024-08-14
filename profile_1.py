import requests
from config import API_TOKEN as token

headers = {"Authorization":token, 
           "Accept":"application/vnd.v1+json"
           }

# $ curl https://whatsapp.turn.io/v1/contacts/27123456789/profile \
#     -H 'Authorization: Bearer token' \
#     -H 'Accept: application/vnd.v1+json'
# > '{
#     "version": "0.0.1-alpha",
#     "schema": "<the-schema-uuid>",
#     "generation": 0,
#     "fields": {
#         "language": "ENG",
#         "date_of_birth": null,
#         "age": 2,
#         "consent": false,
#         "location": null,
#         "name": null,
#         "risk_profile": 2.0,
#         "surname": null,
#         "birthday": null,
#         "opted_in": false,
#         "opted_in_at": null,
#         "whatsapp_id": null,
#         "whatsapp_profile_name": null
#     }
# }'




def get_user_profile(contact, id):
    url = f"https://whatsapp.turn.io/v1/contacts/{contact}/profile"
    params = {"schema": id}

    res = requests.get(url, headers=headers, params=params)
    print(res.text)

    