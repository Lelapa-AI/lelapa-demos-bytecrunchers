import signal
import sys
from db.user_profile_manager importUserProfileDatabaseManager

'''gracefully closes database connection when program is not terminated properly'''
def signal_handler(sig, frame):
    ifUserProfileDatabaseManager.connectionToDB != None:
       UserProfileDatabaseManager.connectionToDB.close() 
    sys.exit(0) 


signal.signal(signal.SIGINT, signal_handler)
