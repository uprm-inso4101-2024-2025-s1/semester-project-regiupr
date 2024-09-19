#import students.py file as student

from DB_connection import StudentsM

def start_profile_conn():
    #similar to Login_backend, we create a global variable with the connection to the database if one is not connected
    global connection
    connection = StudentsM.create_connection()

def get_student_data(student_id):
    #fetch data and return it in an easy to access format (dictionary)
    student_data = StudentsM.fetch_student(connection, student_id)
    characteristics = ["student_id", "name", "email", "birthdate", "ssn", "password"]
    student_data = dict(zip(characteristics,student_data))
    return student_data

