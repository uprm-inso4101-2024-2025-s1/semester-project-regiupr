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

def create_student_course(connection, student_id, course_code, section_id, status):
    cursor = connection.cursor()

    # Check if the course exists
    try:
        cursor.execute(f"SELECT * FROM courses WHERE course_code='{course_code}'")
        course = cursor.fetchone()
        if not course:
            print(f"Course with code {course_code} does not exist")
            return
    except Error as e:
        print(f"Error fetching course with code {course_code}: {e}")
        return
    
    # If the course exists, add the student to the student_courses table
    try:
        cursor.execute(f"INSERT INTO student_courses (student_id, course_code, section_id, status) VALUES ('{student_id}', '{course_code}', '{section_id}', '{status}')")
        connection.commit()
        print(f"Student {student_id} added successfully")
    except Error as e:
        print(f"Error adding student {student_id}: {e}")
    finally:
        cursor.close()

def fetch_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM student_courses")
        student_courses = cursor.fetchall()
        for student_course in student_courses:
            print(student_course)
    except Error as e:
        print(f"Error fetching table: {e}")
    finally:
        cursor.close()

def fetch_student_courses(connection, student_id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT * FROM student_courses WHERE student_id='{student_id}'")
        student_courses = cursor.fetchall()
        for student_course in student_courses:
            print(student_course)
    except Error as e:
        print(f"Error fetching student courses: {e}")
    finally:
        cursor.close()

def update_student_course(connection, student_id, course_code, data, value):
    cursor = connection.cursor()
    try:
        cursor.execute(f"UPDATE student_courses SET {data} = '{value}' WHERE student_id = '{student_id}' AND course_code = '{course_code}'")
        connection.commit()
        print(f"Student {student_id} updated successfully")
    except Error as e:
        print(f"Error updating student {student_id}: {e}")
    finally:
        cursor.close()

def delete_student_course(connection, student_id, course_code):
    cursor = connection.cursor()
    try:
        cursor.execute(f"DELETE FROM student_courses WHERE student_id = '{student_id}' AND course_code = '{course_code}'")
        connection.commit()
        print(f"Course {course_code} deleted successfully")
    except Error as e:
        print(f"Error deleting student {student_id}: {e}")
    finally:
        cursor.close()

def fetch_enrolled_courses(connection, student_id):
    cursor = connection.cursor()
    try:
        # Get all courses for the student with status 'Enrolled'
        query = "SELECT * FROM student_courses WHERE student_id=%s AND status='CURRENTLY TAKING'"
        cursor.execute(query, (student_id,))
        student_courses = cursor.fetchall()

        enrolled_courses = []
        for student_course in student_courses:
            # Fetch course details directly using the course_code
            course_code = student_course[1]
            course_cursor = connection.cursor()
            try:
                # Query to fetch course details from the courses table
                course_query = "SELECT * FROM courses WHERE course_code=%s"
                course_cursor.execute(course_query, (course_code,))
                course = course_cursor.fetchone()

                # If the course exists, append it to the list
                if course:
                    enrolled_courses.append(course)

            except Error as e:
                print(f"Error fetching course details for course code {course_code}: {e}")
            finally:
                course_cursor.close()

        # Return a list of courses
        return enrolled_courses

    except Error as e:
        print(f"Error fetching enrolled courses: {e}")
        return []
    finally:
        cursor.close()

def calculate_total_credits(connection, course_codes):
    cursor = connection.cursor()
    try:
        formatted_course_codes = ', '.join(f"'{code}'" for code in course_codes)
        
        # Query to sum the credits of the specified courses
        cursor.execute(f"""
            SELECT SUM(credits) AS total_credits
            FROM courses
            WHERE course_code IN ({formatted_course_codes})
        """)
        
        result = cursor.fetchone()
        total_credits = result[0] if result else 0
        print(f"Total credits for courses {course_codes}: {total_credits}")
        return total_credits
    except Error as e:
        print(f"Error calculating total credits for courses {course_codes}: {e}")
        return 0
    finally:
        cursor.close()

def calculate_total_credits(connection, curriculum_id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"""
            SELECT SUM(c.credits) AS total_credits
            FROM curriculum_courses cc
            JOIN courses c ON cc.course_code = c.course_code
            WHERE cc.curriculum_id = '{curriculum_id}'
        """)
        result = cursor.fetchone()
        total_credits = result[0] if result else 0
        print(f"Total credits for curriculum {curriculum_id}: {total_credits}")
        return total_credits
    except Error as e:
        print(f"Error calculating total credits for curriculum {curriculum_id}: {e}")
        return 0
    finally:
        cursor.close()




def main():
    connection = create_connection()
    if connection:
        fetch_table(connection)   
        # Step 2: Add some students to the student_courses table
        create_student_course(connection, 'S001', 'CS101', 'A', 'Enrolled')
        create_student_course(connection, 'S001', 'CS102', 'B', 'Enrolled')
        create_student_course(connection, 'S002', 'CS103', 'C', 'Completed')
        create_student_course(connection, 'S002', 'CS104', 'D', 'Enrolled')
        
        # Step 3: Fetch and print all student courses
        print("\nAll student courses:")
        fetch_table(connection)
        
        # Step 4: Fetch and print courses for a specific student (student_id=1)
        print("\nCourses for student with ID S001:")
        fetch_student_courses(connection, 'S001')
        
        # Step 5: Update the status of a course for student_id=1
        print("\nUpdating status for student 1 in course CS101 to 'Completed':")
        update_student_course(connection, 'S001', 'CS101', 'status', 'Completed')
        
        # Step 6: Fetch and print updated courses for student_id=1
        print("\nUpdated courses for student with ID S001:")
        fetch_student_courses(connection, 'S001')
        
        # Step 7: Delete a specific student course for student_id=2
        print("\nDeleting courses for student with ID S002:")
        delete_student_course(connection, 'S002', 'CS101')
        
        # Step 8: Fetch and print the table after deletion
        print("\nTable after deleting student with ID S002:")
        fetch_table(connection)
        
        # Step 9: Fetch and print all courses for student_id=1 with status 'Enrolled'
        print("\nEnrolled courses for student with ID 802-00-0000:")
        enrolled_courses = fetch_enrolled_courses(connection, '802-00-0000')
        for course in enrolled_courses:
            print(course)
        
        # Close the connection
        connection.close()

if __name__ == '__main__':
    main()