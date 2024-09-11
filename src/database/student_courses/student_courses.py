import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='J3SSY-ANDU'
        )
        if connection.is_connected():
            print("Successfully connected to MySQL Platform")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None
    
def create_table(connection, db_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"USE {db_name}")
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS student_courses (
            student_id VARCHAR(255) NOT NULL,
            course_code VARCHAR(255),
            section_id VARCHAR(255),
            status VARCHAR(255),
            FOREIGN KEY (student_id) REFERENCES students(student_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
        )
        '''
        cursor.execute(create_table_query)
        print(f"Table `student_courses` created successfully in database `{db_name}`")
    except Error as e:
        print(f"Error creating cursor: {e}")
    finally:
        cursor.close()

def create_student_course(connection, db_name, student_id, course_code, section_id, status):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"INSERT INTO student_courses (student_id, course_code, section_id, status) VALUES ('{student_id}', '{course_code}', '{section_id}', '{status}')")
        connection.commit()
        print(f"Student {student_id} added successfully")
    except Error as e:
        print(f"Error adding student {student_id}: {e}")
    finally:
        cursor.close()

def fetch_table(connection, db_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        cursor.execute("SELECT * FROM student_courses")
        student_courses = cursor.fetchall()
        for student_course in student_courses:
            print(student_course)
    except Error as e:
        print(f"Error fetching table: {e}")
    finally:
        cursor.close()

def fetch_student_courses(connection, db_name, student_id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"SELECT * FROM student_courses WHERE student_id='{student_id}'")
        student_courses = cursor.fetchall()
        for student_course in student_courses:
            print(student_course)
    except Error as e:
        print(f"Error fetching student courses: {e}")
    finally:
        cursor.close()

def update_student_course(connection, db_name, student_id, course_code, data, value):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"UPDATE student_courses SET {data} = '{value}' WHERE student_id = '{student_id}' AND course_code = '{course_code}'")
        connection.commit()
        print(f"Student {student_id} updated successfully")
    except Error as e:
        print(f"Error updating student {student_id}: {e}")
    finally:
        cursor.close()

def delete_table(connection, db_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        cursor.execute("DROP TABLE student_courses")
        print(f"Table `student_courses` dropped successfully")
    except Error as e:
        print(f"Error dropping table: {e}")
    finally:
        cursor.close()

def delete_student_course(connection, db_name, student_id, course_code):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"DELETE FROM student_courses WHERE student_id = '{student_id}' AND course_code = '{course_code}'")
        connection.commit()
        print(f"Student {student_id} deleted successfully")
    except Error as e:
        print(f"Error deleting student {student_id}: {e}")
    finally:
        cursor.close()

def main():
    db_name = 'regi_upr'
    connection = create_connection()
    if connection:
        # Step 1: Create the table
        print("\n")
        create_table(connection, db_name)
        
        # Step 2: Add some students to the student_courses table
        create_student_course(connection, db_name, 'S123', 'CS101', 'A', 'Enrolled')
        create_student_course(connection, db_name, 'S123', 'CS102', 'B', 'Enrolled')
        create_student_course(connection, db_name, 'S124', 'CS103', 'C', 'Completed')
        create_student_course(connection, db_name, 'S124', 'CS104', 'D', 'Enrolled')
        
        # Step 3: Fetch and print all student courses
        print("\nAll student courses:")
        fetch_table(connection, db_name)
        
        # Step 4: Fetch and print courses for a specific student (student_id=1)
        print("\nCourses for student with ID 1:")
        fetch_student_courses(connection, db_name, 'S123')
        
        # Step 5: Update the status of a course for student_id=1
        print("\nUpdating status for student 1 in course CS101 to 'Completed':")
        update_student_course(connection, db_name, 'S123', 'CS101', 'status', 'Completed')
        
        # Step 6: Fetch and print updated courses for student_id=1
        print("\nUpdated courses for student with ID 1:")
        fetch_student_courses(connection, db_name, 'S123')
        
        # Step 7: Delete a specific student course for student_id=2
        print("\nDeleting courses for student with ID 2:")
        delete_student_course(connection, db_name, 'S123', 'CS101')
        
        # Step 8: Fetch and print the table after deletion
        print("\nTable after deleting student with ID 2:")
        fetch_table(connection, db_name)
        
        # Step 9: Drop the student_courses table
        print("\nDropping the table `student_courses`:")
        delete_table(connection, db_name)

        # Close the connection
        connection.close()

if __name__ == '__main__':
    main()