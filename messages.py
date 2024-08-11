# $ curl -X POST "https://whatsapp.turn.io/v1/messages" \
#   -H "Authorization: Bearer token" \
#   -H "Content-Type: application/json" \
#   -d '
#     {
#         "preview_url": false | true,
#         "recipient_type": "individual",
#         "to": "whatsapp-id",
#         "type": "text",
#         "text": {
#             "body": "your-text-message-content"
#         }
#     }'


# > {
#   "messages": [{
#     "id": "gBEGkYiEB1VXAglK1ZEqA1YKPrU"
#   }]
# }

import requests

token = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJUdXJuIiwiZXhwIjoxNzIzOTAzMDcyLCJpYXQiOjE3MjMyOTgyNzIsImlzcyI6IlR1cm4iLCJqdGkiOiJiYmZiZDIxYy1hMTRmLTQwNjktOGY4Zi0yZGZhN2RkNWM0N2EiLCJuYmYiOjE3MjMyOTgyNzEsInN1YiI6Im51bWJlcjo1OTk0IiwidHlwIjoiYWNjZXNzIn0.hAZXHYuGivuJSt8dTtJ_fbcIYER7vzsi1j8U_1BF0g4EAAfHCIoYi6hGyVwWeH3SvtmnWmhTAHfblEM-O5qNkw"
url = "https://whatsapp.turn.io/v1/messages"

headers = {"Authorization": token, "Content-Type":"application/json"}
data = {"preview_url": False | True, 
        "recepient_type":"individual", 
        "from":"27671401556",
        "type":"text"
        }

res = requests.post(url, headers=headers, json=data)
print(res.text)
