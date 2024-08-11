# curl -X POST https://whatsapp.turn.io/v1/contacts/schemas \
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


import requests

url = "https://whatsapp.turn.io/v1/contacts/schemas"

token = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJUdXJuIiwiZXhwIjoxNzIzOTAzMDcyLCJpYXQiOjE3MjMyOTgyNzIsImlzcyI6IlR1cm4iLCJqdGkiOiJiYmZiZDIxYy1hMTRmLTQwNjktOGY4Zi0yZGZhN2RkNWM0N2EiLCJuYmYiOjE3MjMyOTgyNzEsInN1YiI6Im51bWJlcjo1OTk0IiwidHlwIjoiYWNjZXNzIn0.hAZXHYuGivuJSt8dTtJ_fbcIYER7vzsi1j8U_1BF0g4EAAfHCIoYi6hGyVwWeH3SvtmnWmhTAHfblEM-O5qNkw"



header = {
    'Authorization': token, 
    'Accept':'application/vnd.v1+json', 
    'Content-Type':'application/json'
}

data = {
    'version':'0.0.1-alpha', 
    'fields':[{
            "name": "consent",
            "display": "Consent Given",
            "type": "BOOLEAN",
            "default": False,
            "is_private": True
    }]
}

res = requests.post(url, headers=header, json=data)
print(res.text)