from DB_connection import StudentsM 

def start_login():
    connection = StudentsM.create_connection()
    if connection:
        connection.close()

start_login()