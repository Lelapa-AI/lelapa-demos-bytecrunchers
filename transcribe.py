import os
import base64
import requests
import time 
from flask import Flask, request, jsonify
from retry_requests import retry
from requests import Session
from audio_retriever import retrieve_media
from vulavula import VulavulaClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Get your VULAVULA_TOKEN by logging in and getting keys
VULAVULA_TOKEN = os.getenv("VULAVULA_TOKEN")

# Our headers for authentication
headers = {
    "X-CLIENT-TOKEN": VULAVULA_TOKEN,
}

# The transport API to upload your file
TRANSPORT_URL = "https://vulavula-services.lelapa.ai/api/v1/transport/file-upload"

# The transcribe API URL to kick off your transcription job.
TRANSCRIBE_URL = "https://vulavula-services.lelapa.ai/api/v1/transcribe/process/"

# The webhook URL now points to our own Flask endpoint (second one)
WEBHOOK_URL = "http://127.0.0.1:5000/transcription-webhook"

# Retry requests configuration
session = retry(Session(), retries=3, backoff_factor=0.5)


# First endpoint: Receives a link to a file and processes it
@app.route('/file-link', methods=['POST'])
def receive_file_link():
    try :
        data = request.get_json()
        media_id = data.get('media_id')

        if not media_id or not os.path.exists(media_id):
            return jsonify({"error": "No valid media ID or access token provided"}), 400

        # Retrieve media file 
        file_path = retrieve_media(media_id)


        client = VulavulaClient(VULAVULA_TOKEN)

        upload_id, transcription_result = client.transcribe(
            file_path, 
            webhook = WEBHOOK_URL
        )

        print("upload id: ", upload_id)
        print("Transcription Submit Success: ", transcription_result) #A success message, data is sent to webhook
        
        while client.get_transcribed_text(upload_id)['message'] == "Item has not been processed.":
            time.sleep(5)
            print("Waiting for transcribe to complete...")
        response = client.get_transcribed_text(upload_id)
        print(response)


        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)