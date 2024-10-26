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

# Adds a new course entry to the 'courses' table with the given details
def create_course(connection, course_code, course_name, description, credits, program):
    cursor = connection.cursor()
    try:
        cursor.execute(f"INSERT INTO courses (course_code, course_name, description, credits, program) VALUES ('{course_code}', '{course_name}', '{description}', {credits}, '{program}')")
        connection.commit()
        print(f"Course {course_name} added successfully")
    except Error as e:
        print(f"Error adding course {course_name}: {e}")
    finally:
        cursor.close()

# Fetches and prints all entries from the 'courses' table
def fetch_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        for course in courses:
            print(course)
        return courses
    except Error as e:
        print(f"Error fetching table: {e}")
    finally:
        cursor.close()

# Fetches and prints a specific course from the 'courses' table based on the provided course code
def fetch_course(connection, course_code):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT * FROM courses WHERE course_code='{course_code}'")
        course = cursor.fetchone()
        print(f"Course with code {course_code}: {course}")
        return course
    except Error as e:
        print(f"Error fetching course with code {course_code}: {e}")
    finally:
        cursor.close()

# Updates a specific field of a course entry in the 'courses' table for a given course code
def update_course(connection, course_code, data, value):
    cursor = connection.cursor()
    try:
        cursor.execute(f"UPDATE courses SET {data} = '{value}' WHERE course_code = '{course_code}'")
        connection.commit()
    except Error as e:
        print(f"Error updating course with code {course_code}: {e}")
    finally:
        cursor.close()

# Deletes a specific course from the 'courses' table based on the provided course code
def delete_course(connection, course_code):
    cursor = connection.cursor()
    try:
        cursor.execute(f"DELETE FROM courses WHERE course_code = '{course_code}'")
        connection.commit()
        print(f"Course with code {course_code} deleted successfully")
    except Error as e:
        print(f"Error deleting course with code {course_code}: {e}")
    finally:
        cursor.close()

# The main() is to test each of the CRUD functions
def main():
    connection = create_connection()
    if connection:
        fetch_table(connection)

        # Adding dummy courses for testing
        #create_course(connection, 'CIIC3015', "Introduction to Computer Programming I", "Analysis of algorithmic problems, development of solutions, and their implementation in a high level programming language using object-oriented programming techniques.", '3', "CIIC")
        #create_course(connection, 'CIIC4010', "Advanced Programming", "Advanced programming techniques applied to the solution of engineering problems, extensive use of subprograms, logical and specifications statements. Principles of multiprogramming, multiprocessing, and real-time systems.", '3', "CIIC")
        ##create_course(connection, 'CIIC4020', "Data Structures", "Data structures in programming languages; representation of information as data lists in linear, orthogonal, string, and array form; tree structures; techniques for storage allocation, distribution collection, and sorting of data.", '3', "CIIC")
        #create_course(connection, 'INSO4101', "Introduction to Software Engineering", "Introduction to the software development cycle. Models for the software development process and related metrics. Ethical issues in software engineering.", '3', "INSO")

        # Fetching and displaying all courses in the database
        #print("\nAll courses offered:")
        #fetch_table(connection)

        # Fetching and displaying a specific course by its code
        print("\nFetching course with code CIIC3015: ")
        fetch_course(connection, 'LING4010')

        # Updating the credit value of a specific course
        #print("\nUpdating course CIIC3015: ")
        #update_course(connection, 'CIIC3015', 'credits', '4')

        # Deleting a specific course from the database
        #print("\nDeleting course CIIC4010: ")
        #delete_course(connection, 'CIIC4010')

        # Fetching and displaying all courses after deletion
        #print("\nAll courses offered after deletion:")
        #fetch_table(connection)
        
        connection.close()

if __name__ == "__main__":
    main()