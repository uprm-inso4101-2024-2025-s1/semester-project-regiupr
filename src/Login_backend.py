from DB_connection import StudentsM 

# Connection to be established with the database server.
global connection

# This item is used by other modules with display logged student's info to know which student info has to be displayed.
global students_id

def verify_credentials(username, student_id, password):

    # This verify that the student id provided by the user is in the database when given as arguments to the fetch_student method.
    student_list = StudentsM.fetch_table(connection)
    for row in student_list:
        if (row[0] == student_id):
            break
    else:
        return 0
    
    fetched_email = StudentsM.fetch_student(connection, student_id)[2]
    fetched_password = StudentsM.fetch_student(connection, student_id)[5]

    # Notice how the 3rd argument is an integer passed in this function is turned into an integer.
    return (fetched_email == username and fetched_password == int(password))

def start_login():
    #Initialize the global variable for database server connection.
    connection = StudentsM.create_connection()

    # Two dummy student's data to be used as an example.
    StudentsM.create_student(connection, "802-12-3456", "Juan Lopez", "student.name@upr.edu", "1998-01-15", 123456700, 1234)
    StudentsM.create_student(connection, "802-21-6890", "Kiara Gonzales", "kiara.gonzales@upr.edu", "1998-01-15", 123456780, 5678)

def end_session():
     if connection:
        connection.close()