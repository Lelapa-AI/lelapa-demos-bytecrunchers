from flask import Flask, request, jsonify
import requests
from update import *



app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def handle_get():
    whatsapp_id = request.args.get('whatsapp_id')
    print(f"Received whatsapp_id: {whatsapp_id}")

    response = update_user_profile_name(whatsapp_id, name)
    print("===> ", response)

    return jsonify({"status": "success", "name": response.get('fields').get('name'), "whatsapp_id": response.get("fields").get("whatsapp_id")}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8200)
