import sqlite3

'''class performs all functions related to database management of the user profiles that interact with whatsapp bot'''
class UserProfileDatabaseManager:
    cursor_object = None
    connectionToDB = None

    def __init__(self, whatsapp_id, schema_uuid):
        self.whatsapp_id = whatsapp_id
        self.schema_uuid = schema_uuid
        self.connectToDB()
        self.insert_into_db()


    '''connects to DB & initialises cursor object'''
    def connectToDB(self):
        self.connectionToDB = sqlite3.connect("db/profiles.db")
        self.cursor_object = self.connectionToDB.cursor()

    
    '''executes SQL query to update a row'''
    def updateUserProfileOnDb(self):
        # update_query = f'''
        # update user_profiles 
        # set schema_uuid = {self.schema_uuid}
        # where whatsapp_id = {self.whatsapp_id}
        # '''
        update_query = '''
        update user_profiles
        set schema_uuid = ?
        where whatsapp_uuid = ?
        '''
        print(update_query)
        print("==========> ", self.schema_uuid)
        self.cursor_object.execute(update_query, (self.schema_uuid, self.whatsapp_id))
        # self.cursor_object.execute("update user_profiles set schema_uuid = (?)", (self.schema_uuid, self.whatsapp_id))
        self.commitDbQuery()


    
    '''inserts new values into the table on the database'''
    def insert_into_db(self):
        insert_query = f'''
        insert or replace into user_profiles
        values({int(self.whatsapp_id)}, {int(self.schema_uuid)})
        '''
        self.cursor_object.execute(insert_query)
        self.commitDbQuery()
        
    '''sets the new schema_uuid for the profile'''
    def set_new_uuid(self, new_id):
        self.schema_uuid = new_id
        print('+++++++++', new_id)
        self.updateUserProfileOnDb()

    '''commits changes to the database'''
    def commitDbQuery(self):
        self.connectionToDB.commit()


    '''closes the database connection'''
    def closeDbConnection(self):
        self.connectionToDB.close()
        

    def __str__(self):
        return f'{self.schema_uuid} {self.whatsapp_id}'



    