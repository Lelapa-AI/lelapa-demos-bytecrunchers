from flask import Flask, request, jsonify
import requests
from update import *



app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def handle_get():
    # Step 2: Access Query Parameters
    name = request.args.get('name')  # Get the 'name' query parameter
    whatsapp_id = request.args.get('whatsapp_id')  # Get the 'whatsapp_id' query parameter

    # Log the received query parameters
    print(f"Received name: {name}")
    print(f"Received whatsapp_id: {whatsapp_id}")

    response = update_user_profile_name(whatsapp_id, name)
    print("===> ", response)

    # Step 3: Make a GET request to another endpoint, if needed
    # (Optional: use the received data in another request)

    # Step 4: Respond to the request
    return jsonify({"status": "success", "name": response.get('fields').get('name'), "whatsapp_id": response.get("fields").get("whatsapp_id")}), 200
    # return "Done"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8200)  # Run the Flask app
