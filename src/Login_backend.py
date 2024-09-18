from DB_connection import StudentsM 

# This item is used by other modules with display logged student's info to know which student info has to be displayed
global students_id

def start_login():
    global connection
    connection = StudentsM.create_connection()

    # Two dummy student's data to be used as an example
    StudentsM.create_student(connection, "802-24-0812", "Juan Lopez", "juan.lopez1@upr.edu", "1998-01-15", 123456700, 1234)
    StudentsM.create_student(connection, "802-21-6890", "Kiara Gonzales", "kiara.gonzales@upr.edu", "1998-01-15", 123456780, 5678)

    datatest = StudentsM.fetch_student(connection, "802-24-0812")
    print("lmao", datatest)

    #verify_credentials()

    if connection:
        connection.close()

start_login()

def verify_credentials(username, student_id, password):

    StudentsM.fetch_student(connection, student_id)


    if 1:
        return True
    else:
        return False