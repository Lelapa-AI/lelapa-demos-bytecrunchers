from flask import Flask, request, jsonify
import requests
from additional_fields import *
from db.user_profile_manager import UserProfileDatabaseManager
userProfile = None
# from update import *



app = Flask(__name__)

# @app.route('/endpoint', methods=['GET'])
# def handle_get():
#     whatsapp_id = request.args.get('whatsapp_id')
#     print(f"Received whatsapp_id: {whatsapp_id}")

#     response = update_user_profile_manager_name(whatsapp_id, name)
#     print("===> ", response)

#     return jsonify({"status": "success", "name": response.get('fields').get('name'), "whatsapp_id": response.get("fields").get("whatsapp_id")}), 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8200)



@app.route('/create', methods=['GET'])
def handle_get():
    create_consent_field()
    whatsapp_id = request.args.get('whatsapp_id')
    userProfile = UserProfileDatabaseManager(whatsapp_id, 1)
    userProfile.insert_into_db()
    # print(request)
    # TODO: create a function to check the arguments passed
    # if key elements are missing, set to None or retrieve the values stored inside
    # response = update_user_profile_manager_name(whatsapp_id, name)

    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8200)



# TODO: close the database connection at the end the execution of the flask app