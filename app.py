import profile_1
from flask import Flask, request, jsonify
from arg_processor import * 
import requests
from additional_fields import *
from db.user_profile_manager import UserProfileDatabaseManager
from db.user_profile import UserProfile
userProfile = None
from update_profile import *
holder = ["age", "surname", "name"]
myHolder = {}
my_new_switch = ArgumentProcessor()




app = Flask(__name__)


@app.route('/create', methods=['GET'])
def myDisplay():

    ageCheck = request.args
    # print("===> ", len(request.args.get("age", "Nothing in there").strip()))

    processVars(ageCheck)


    # return (len(request.args.get("name").strip()) > 5).json(), 200
    return "Returned", 200





def processVars(args):


    for arg in args:
        if arg in holder:
            print(my_switch.trait(arg, args))

    print("Done")
    # print(myHolder)




# @app.route('/create', methods=['GET'])
def add_user_to_db():
    create_consent_field()
    print("===>", request)
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

    return "", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8200)



# TODO: close the database connection at the end the execution of the flask app