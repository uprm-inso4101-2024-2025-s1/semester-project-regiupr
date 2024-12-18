from DB_connection import StudentsM 
import configparser
import mysql.connector

def verify_credentials(username, student_id, password):
    config = configparser.ConfigParser()
    config.read('credentials/db_config.ini')
    db_connection = mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database']
    )

    # This verify that the student id provided by the user is in the database when given as arguments to the fetch_student method.
    student_list = StudentsM.fetch_table(db_connection)
    for row in student_list:
        if (row[0] == student_id):
            global student_id_access
            student_id_access = student_id
            break
    else:
        return 0
    
    global student
    student = StudentsM.fetch_student(db_connection, student_id)
    #fetched_email = StudentsM.fetch_student(connection, student_id)[2] : student[2]
    #fetched_password = StudentsM.fetch_student(connection, student_id)[5] : student[5]

    # Notice how the 3rd argument is an integer passed in this function is turned into an integer. Currently, the database 
    # has not been reestructured to be able to store passwords as integers.
    return (student[2] == username and (student[5] if isinstance(password, int) else str(student[5])) == password)

# if the user logs to an account successfully, this will return the id of the student so that other modules
# know which studnet information they have to access.
def get_student_id():
    return student_id_access
 
def get_student_info_by_id(student_id):
    return StudentsM.fetch_student(connection, student_id)

def get_student_info():
    return student

def start_login():
    #Declaration and initialization of the global variable for database server connection.
    global connection
    connection = StudentsM.create_connection()

    # Dummy student's data to be used as an example. They are commented because they are already on the database. You can read
    # this to know what there are there. 
    # StudentsM.create_student(connection, "802-12-3456", "Juan Lopez", "juan.lopez@upr.edu", "1998-01-15", 123456700, 1234)
    # StudentsM.create_student(connection, "802-21-0812", "Juan Lopez", "juan.lopez1@upr.edu", "1998-01-15", 123456700, 1234)
    # StudentsM.create_student(connection, "802-21-6890", "Kiara Gonzales", "kiara.gonzales@upr.edu", "1998-01-15", 123456780, 5678)

def end_session():
     if connection:
        connection.close()