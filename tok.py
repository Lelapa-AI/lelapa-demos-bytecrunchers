import requests

# Define the URL
url = "https://whatsapp.turn.io/v1/users/login"

# Define the credentials
auth = ('15550159947', '1rDJk-EHl15vvQez9MUyZdNHYVToO7_2')  # Replace with your actual username and password

# Make the POST request with Basic Auth
response = requests.post(url, auth=auth)

# Print the response
print(response.text)
