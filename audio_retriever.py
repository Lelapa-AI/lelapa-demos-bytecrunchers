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
        # Send a GET request to the URL with headers
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status() 

        # Define the output file name based on media_id
        output_file = f"{media_id}.m4a"

        # Write the content to a file
        with open(output_file, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Media downloaded successfully and saved as {output_file}")

        return output_file
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

        return None

# Example usage
# media_id = "1775875342946237"  # Replace with your actual media ID
 # Replace with your actual access token
# output_file = "retrieved_media.mp3"  # Desired output file name

# retrieve_media(media_id)
