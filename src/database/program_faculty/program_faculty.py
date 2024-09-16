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

# Adds a new entry to the 'program_faculty' table with the given program and faculty values
def create_program_faculty(connection, program, faculty):
    cursor = connection.cursor()
    try:
        cursor.execute(f"INSERT INTO program_faculty (program, faculty) VALUES ('{program}', '{faculty}')")
        connection.commit()
        print(f"Program {program} added successfully")
    except Error as e:
        print(f"Error adding program {program}: {e}")
    finally:
        cursor.close()

# Fetches and prints all entries from the 'program_faculty' table
def fetch_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM program_faculty")
        program_faculty = cursor.fetchall()
        for row in program_faculty:
            print(row)
        return program_faculty
    except Error as e:
        print(f"Error fetching table: {e}")
    finally:
        cursor.close()

# Fetches and prints a specific program-faculty entry based on the provided program code
def fetch_program_faculty(connection, program):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT * FROM program_faculty WHERE program='{program}'")
        program_faculty = cursor.fetchone()
        print(f"Program with code {program}: {program_faculty}")
        return program_faculty
    except Error as e:
        print(f"Error fetching program with code {program}: {e}")
    finally:
        cursor.close()

# Updates a specific field in the 'program_faculty' table for a given program
def update_program_faculty(connection, program, data, value):
    cursor = connection.cursor()
    try:
        cursor.execute(f"UPDATE program_faculty SET {data} = '{value}' WHERE program = '{program}'")
        connection.commit()
    except Error as e:
        print(f"Error updating program {program}: {e}")
    finally:
        cursor.close()

# Deletes a specific program-faculty entry from the 'program_faculty' table based on the provided program code
def delete_program_faculty(connection, program):
    cursor = connection.cursor()
    try:
        cursor.execute(f"DELETE FROM program_faculty WHERE program = '{program}'")
        connection.commit()
    except Error as e:
        print(f"Error deleting program {program}: {e}")
    finally:
        cursor.close()

# The main() is to test each of the CRUD functions
def main():
    connection = create_connection()

    # Add sample program-faculty entries to the table
    create_program_faculty(connection, 'CIIC', 'Engineering')
    create_program_faculty(connection, 'INSO', 'Engineering')

    # Fetch and display all entries in the program-faculty table
    print("All Programs: ")
    fetch_table(connection)

    # Fetch and display a specific entry by program code
    fetch_program_faculty(connection, 'CIIC')

    # Update the faculty for a specific program
    print("Update Program: ")
    update_program_faculty(connection, 'CIIC', 'faculty', 'Biology')

    # Delete a specific program entry
    print("Delete Program: ")
    delete_program_faculty(connection, 'CIIC')

    # Fetch and display all entries after updating and deleting
    print("All Programs after change: ")
    fetch_table(connection)

if __name__ == "__main__":
    main()
