import configparser
import mysql.connector

# fetch data and return it in an easy to access format (dictionary)
def get_student_data(fetched_student):
    config = configparser.ConfigParser()
    config.read('credentials/db_config.ini')
    conn = mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database']
    )
    cursor = conn.cursor()
    
    # Unpack the fetched student details
    characteristics = ["student_id", "name", "email", "birthdate", "ssn", "password"]
    student_data = dict(zip(characteristics, fetched_student))
    student_id = student_data.get("student_id")

    print(f"Student ID for fetching curriculum: {student_id}")  # Debug print statement

    try:
        # Fetch the curriculum_id associated with the student
        query = """
            SELECT curriculum_id
            FROM student_curriculum
            WHERE student_id = %s
        """
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()
        print(f"Query Result for curriculum_id: {result}")  # Debug print statement

        if result is not None:
            # Add curriculum_id to the student_data dictionary
            student_data["curriculum_id"] = result[0]
        else:
            # If no curriculum_id is found, set it to None
            student_data["curriculum_id"] = None

    except mysql.connector.Error as err:
        print(f"Database Error: {str(err)}")

    finally:
        cursor.close()
        conn.close()

    print(f"Final Student Data: {student_data}")  # Debug print statement

    return student_data