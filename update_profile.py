import requests
from config import API_TOKEN as token

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


