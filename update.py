import requests

# curl -X PATCH https://whatsapp.turn.io/v1/contacts/27123456789/profile \
#     -H 'Authorization: Bearer token' \
#     -H 'Accept: application/vnd.v1+json' \
#     -H 'Content-Type: application/json' \
#     -d '{"name": "Fizbo"}'

token = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJUdXJuIiwiZXhwIjoxNzIzOTAzMDcyLCJpYXQiOjE3MjMyOTgyNzIsImlzcyI6IlR1cm4iLCJqdGkiOiJiYmZiZDIxYy1hMTRmLTQwNjktOGY4Zi0yZGZhN2RkNWM0N2EiLCJuYmYiOjE3MjMyOTgyNzEsInN1YiI6Im51bWJlcjo1OTk0IiwidHlwIjoiYWNjZXNzIn0.hAZXHYuGivuJSt8dTtJ_fbcIYER7vzsi1j8U_1BF0g4EAAfHCIoYi6hGyVwWeH3SvtmnWmhTAHfblEM-O5qNkw"
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJUdXJuIiwiZXhwIjoxNzIzOTAzMDcyLCJpYXQiOjE3MjMyOTgyNzIsImlzcyI6IlR1cm4iLCJqdGkiOiJiYmZiZDIxYy1hMTRmLTQwNjktOGY4Zi0yZGZhN2RkNWM0N2EiLCJuYmYiOjE3MjMyOTgyNzEsInN1YiI6Im51bWJlcjo1OTk0IiwidHlwIjoiYWNjZXNzIn0.hAZXHYuGivuJSt8dTtJ_fbcIYER7vzsi1j8U_1BF0g4EAAfHCIoYi6hGyVwWeH3SvtmnWmhTAHfblEM-O5qNkw', 
    'Accept':'application/vnd.v1+json', 
    'Content-Type':'application/json'}



def update_user_profile_name(contact_number, name):
    
    url = f"https://whatsapp.turn.io/v1/contacts/{str(contact_number)}/profile"
    data = {'name': str(name)}
    res = requests.patch(url, headers=headers, json=data)
    print(res)

    return res.json()

