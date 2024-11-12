import mysql.connector
from mysql.connector import Error
import configparser

def create_connection():
    try:
        config = configparser.ConfigParser()
        config.read('credentials/db_config.ini')
        connection = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )
        if connection.is_connected():
            print("Successfully connected to MySQL Platform")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None

def create_student(connection, student_id, name, email, birthdate, ssn, password, general_gpa, specialty_gpa):
    cursor = connection.cursor()
    try:
        # Now we insert the provided student_id as a varchar instead of an auto-incrementing integer
        cursor.execute(f"INSERT INTO students (student_id, name, email, birthdate, ssn, password, general_gpa, specialty_gpa) VALUES ('{student_id}', '{name}', '{email}', '{birthdate}', {ssn}, {password}, {general_gpa}, {specialty_gpa})")
        connection.commit()
        print(f"Student {name} added successfully")
    except Error as e:
        print(f"Error adding student {name}: {e}")
    finally:
        cursor.close()

def fetch_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        #for row in rows:
        #    print(row)
    except Error as e:
        print(f"Error fetching table students: {e}")
    finally:
        cursor.close()
    return rows # Added

def fetch_student(connection, student_id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT * FROM students WHERE student_id = '{student_id}'")
        student = cursor.fetchone()
        # print(f"Student with ID {student_id}: {student}")
    except Error as e:
        print(f"Error fetching student with ID {student_id}: {e}")
    finally:
        cursor.close()
    return student # Added for having a way to access the student info

def update_student(connection, student_id, data, value):
    cursor = connection.cursor()
    try:
        cursor.execute(f"UPDATE students SET {data} = '{value}' WHERE student_id = '{student_id}'")
        connection.commit()
        print(f"Student with ID {student_id} updated successfully")
    except Error as e:
        print(f"Error updating student with ID {student_id}: {e}")
    finally:
        cursor.close()

def delete_student(connection, student_id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"DELETE FROM students WHERE student_id = '{student_id}'")
        connection.commit()
        print(f"Student with ID {student_id} deleted successfully")
    except Error as e:
        print(f"Error deleting student with ID {student_id}: {e}")
    finally:
        cursor.close()

def fetch_general_gpa(connection, student_id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT general_gpa FROM students WHERE student_id = '{student_id}'")
        general_gpa = cursor.fetchone()
        if general_gpa:
            print(f"General GPA for student {student_id}: {general_gpa[0]}")
            return general_gpa[0]
        else:
            print(f"No General GPA found for student {student_id}")
            return None
    except Error as e:
        print(f"Error fetching General GPA for student with ID {student_id}: {e}")
    finally:
        cursor.close()

def fetch_specialty_gpa(connection, student_id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT specialty_gpa FROM students WHERE student_id = '{student_id}'")
        specialty_gpa = cursor.fetchone()
        if specialty_gpa:
            print(f"Specialty GPA for student {student_id}: {specialty_gpa[0]}")
            return specialty_gpa[0]
        else:
            print(f"No Specialty GPA found for student {student_id}")
            return None
    except Error as e:
        print(f"Error fetching Specialty GPA for student with ID {student_id}: {e}")
    finally:
        cursor.close()

def fetch_remaining_credits(connection, student_id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"""
            SELECT c.total_credits - sc.completed_credits AS remaining_credits
            FROM curriculum c
            JOIN student_curriculum sc ON sc.curriculum_id = c.curriculum_id
            WHERE sc.student_id = '{student_id}'
        """)
        result = cursor.fetchone()
        remaining_credits = result[0] if result else 0
        print(f"Remaining credits for student {student_id}: {remaining_credits}")
        return remaining_credits
    except Error as e:
        print(f"Error fetching remaining credits for student with ID {student_id}: {e}")
        return 0
    finally:
        cursor.close()


def main():
    connection = create_connection()
    if connection:
        # Step 1: Add students with specific string IDs
        print("\n")    
        create_student(connection, "S001", "John Doe", "johndoe@example.com", "1998-01-15", 123456789, 1234, 3.5, 3.7)
        create_student(connection, "S002", "Kevin Doe", "kevin@example.com", "1995-05-20", 123456789, 2345, 3.7, 3.9)
        create_student(connection, "S003", "Jane Doe", "jane@example.com", "1997-07-15", 987654321, 3456, 3.9, 4.0)
        
        # # Step 4: Fetch and print table data
        print("\nStudent table data:")
        fetch_table(connection)
        
        # # Step 6: Fetch and print a specific student by ID
        print("\nFetch student with ID S001:")
        fetch_student(connection, "S001")
        
        # # Step 7: Update a student's email
        print("\nUpdate student with ID S003's email:")
        update_student(connection, "S003", "email", "updated@example.com")
        
        # # Step 8: Fetch updated student
        print("\nFetch updated student with ID S003:")
        fetch_student(connection, "S003")
        
        # # Step 9: Delete a student
        print("\nDelete student with ID S003:")
        delete_student(connection, "S003")
        
        # # Step 10: Fetch and print updated table data
        print("\nUpdated student table data:")
        fetch_table(connection)

        # # Close the connection
        connection.close()

if __name__ == "__main__":
    main()
