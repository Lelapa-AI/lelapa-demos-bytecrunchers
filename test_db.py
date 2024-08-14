from database_management import UserProfile

# import sqlite3

# def main():
#     dbCursor = connectToDB()
#     insert_values_into_table(890, 0000, dbCursor)


    
#     pass

# '''function connects to the database and returns a cursor object pointing to the database'''
# def connectToDB():
#     connectionToDB = sqlite3.connect('profiles.db')
#     cursor_object = connectionToDB.cursor()
#     return cursor_object

# '''insert new values into database table'''
# def insert_values_into_table(whatsapp_id, new_schema_uuid, cursor_object):

#     insert_query = f"""
#     INSERT INTO USER_PROFILES VALUES({whatsapp_id}, {new_schema_uuid})
#     """
#     cursor_object.execute(insert_query)
#     cursor_object.commit()
#     cursor_object.close()
    

# if __name__ == "__main__":
#     main()

my_user = UserProfile(670, 556)
my_user.connectToDB()
my_user.updateUserProfile(000)
my_user.commitAndClose()
