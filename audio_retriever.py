import requests
import os
from dotenv import load_dotenv

load_dotenv()

def retrieve_media(media_id):
    access_token = os.getenv("TURN")
    url = f"https://whatsapp.turn.io/v1/media/{media_id}"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    try:
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status() 

        output_file = f"{media_id}.m4a"

        with open(output_file, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Media downloaded successfully and saved as {output_file}")

        return output_file
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

        return None
