import os
import time 
from flask import Flask, request, jsonify
from retry_requests import retry
from requests import Session
from audio_retriever import retrieve_media
from vulavula import VulavulaClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

VULAVULA_TOKEN = os.getenv("VULAVULA_TOKEN")

WEBHOOK_URL = "http://127.0.0.1:5000/transcription-webhook"

session = retry(Session(), retries=3, backoff_factor=0.5)


# First endpoint: Receives a link to a file and processes it
@app.route('/media-id', methods=['POST'])
def receive_media_id():
    try :
        data = request.get_json()
        media_id = data.get('media_id')

        if not media_id or not os.path.exists(media_id):
            return jsonify({"error": "No valid media ID or access token provided"}), 400

        file_path = retrieve_media(media_id)

        client = VulavulaClient(VULAVULA_TOKEN)

        upload_id, transcription_result = client.transcribe(
            file_path, 
            webhook = WEBHOOK_URL
        )

        print("upload id: ", upload_id)
        print("Transcription Submit Success: ", transcription_result)
        
        while client.get_transcribed_text(upload_id)['message'] == "Item has not been processed.":
            time.sleep(5)
            print("Waiting for transcribe to complete...")
        response = client.get_transcribed_text(upload_id)
        print(response)


        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/transcription-webhook', methods=['POST'])
def receive_transcription_results():
    try:
        data = request.get_json()
        file_id = data.get('file_id')
        transcription_status = data.get('status')
        transcription_results = data.get('results')

        if not file_id or not transcription_status:
            return jsonify({"error": "Invalid data from webhook"}), 400

        return jsonify({"message": "Transcription results received successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True)