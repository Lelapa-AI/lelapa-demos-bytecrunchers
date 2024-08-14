import sqlite3

'''class performs all functions related to database management of the user profiles that interact with whatsapp bot'''
class UserProfileDatabaseManager:
    cursor_object = None
    connectionToDB = None

    def __init__(self, whatsapp_id, schema_uuid):
        self.whatsapp_id = whatsapp_id
        self.schema_uuid = schema_uuid
        self.connectToDB()


    '''connects to DB & initialises cursor object'''
    def connectToDB(self):
        self.connectionToDB = sqlite3.connect("profiles.db")
        self.cursor_object = self.connectionToDB.cursor()

    
    '''executes SQL query to update a row'''
    def updateUserProfile(self, new_schema_uuid):
        update_query = f'''
        update user_profiles 
        set schema_uuid = {new_schema_uuid}
        where whatsapp_id = {self.whatsapp_id}
        '''
        self.cursor_object.execute(update_query)
        self.commitDbQuery()

        # TODO: add code to add new schema id to database here

        # new_schema = response.json().schema 

    
    '''inserts new values into the table on the database'''
    def insert_into_db(self):
        insert_query = f'''
        insert into user_profiles
        values({self.whatsapp_id}, {self.schema_uuid})
        '''
        self.cursor_object.execute(insert_query)
        self.commitDbQuery()
        
    '''sets the new schema_uuid for the profile'''
    def set_new_uuid(self, new_id):
        self.schema_uuid = new_id

    '''commits changes to the database'''
    def commitDbQuery(self):
        self.connectionToDB.commit()


    '''closes the database connection'''
    def closeDbConnection(self):
        self.connectionToDB.close()
        

    def __str__(self):
        return f'{self.schema_uuid} {self.whatsapp_id}'



    