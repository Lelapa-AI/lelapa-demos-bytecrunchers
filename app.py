import profile_1
from flask import Flask, request, jsonify
import requests
from additional_fields import *
from db.user_profile_manager import UserProfileDatabaseManager
from db.user_profile import UserProfile
userProfile = None
from update_profile import *



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
def add_user_to_db():
    create_consent_field()

    usr = UserProfile(request)
    my_manager = UserProfileDatabaseManager(usr.w_id, 0)
    new_schema_id = update_whatsapp_profile_info(usr)
    my_manager.set_new_uuid(new_schema_id)
    print("SEt !")
    profile_1.get_user_profile(usr.w_id, new_schema_id)
    print("Got")




    print("........", usr.location)
    

    # TODO: update the user profile according to the args extracted, use the schema uuid returned from that function to update the schema_uuid for the whatsapp_id on the database
    # TODO: each time we call the retrieve profile, access db to get the schema_uuid for the whatsapp id 

    
    
    
    
    # whatsapp_id = request.args.get('user_profile')
    
    # print("===> ", type(whatsapp_id.args))
    # userProfile = UserProfileDatabaseManager(whatsapp_id, 1)
    # userProfile.insert_into_db()
    # print(request)
    # TODO: create a function to check the arguments passed
    # if key elements are missing, set to None or retrieve the values stored inside
    # response = update_user_profile_manager_name(whatsapp_id, name)

    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8200)



# TODO: close the database connection at the end the execution of the flask app