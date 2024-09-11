import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='J3SSY-ANDU',
        )
        if connection.is_connected():
            print("Successfully connected to MySQL Platform")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return None

def create_database(connection, db_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database `{db_name}` created successfully")
    except Error as e:
        print(f"Error creating database {db_name}: {e}")
    finally:
        cursor.close()

def create_table(connection, db_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"USE {db_name}")
        # Change student_id to VARCHAR(255) and make it the primary key
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            student_id VARCHAR(255) PRIMARY KEY, 
                            name VARCHAR(255) NOT NULL, 
                            email VARCHAR(255) NOT NULL, 
                            birthdate DATE NOT NULL, 
                            ssn INT NOT NULL, 
                            password VARCHAR(255) NOT NULL
                          )''')
        print(f"Table `students` created successfully in database `{db_name}`")
    except Error as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()

def create_student(connection, db_name, student_id, name, email, birthdate, ssn, password):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        # Now we insert the provided student_id as a varchar instead of an auto-incrementing integer
        cursor.execute(f"INSERT INTO students (student_id, name, email, birthdate, ssn, password) VALUES ('{student_id}', '{name}', '{email}', '{birthdate}', {ssn}, '{password}')")
        connection.commit()
        print(f"Student {name} added successfully")
    except Error as e:
        print(f"Error adding student {name}: {e}")
    finally:
        cursor.close()

def fetch_db(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    for db in databases:
        print(db)

def fetch_table(connection, db_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error fetching table students: {e}")
    finally:
        cursor.close()

def fetch_student(connection, db_name, student_id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"SELECT * FROM students WHERE student_id = '{student_id}'")
        student = cursor.fetchone()
        print(f"Student with ID {student_id}: {student}")
    except Error as e:
        print(f"Error fetching student with ID {student_id}: {e}")
    finally:
        cursor.close()

def update_student(connection, db_name, student_id, data, value):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"UPDATE students SET {data} = '{value}' WHERE student_id = '{student_id}'")
        connection.commit()
        print(f"Student with ID {student_id} updated successfully")
    except Error as e:
        print(f"Error updating student with ID {student_id}: {e}")
    finally:
        cursor.close()

def delete_table(connection, db_name, table_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        print(f"Table `{table_name}` deleted successfully")
    except Error as e:
        print(f"Error deleting table {table_name}: {e}")
    finally:
        cursor.close()

def delete_student(connection, db_name, student_id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"DELETE FROM students WHERE student_id = '{student_id}'")
        connection.commit()
        print(f"Student with ID {student_id} deleted successfully")
    except Error as e:
        print(f"Error deleting student with ID {student_id}: {e}")
    finally:
        cursor.close()

def main():
    db_name = "regi_upr"
    connection = create_connection()
    if connection:
        # Step 1: Create the database
        print("\n")
        create_database(connection, db_name)
        
        # Step 2: Create the table
        create_table(connection, db_name)
        
        # Step 3: Add students with specific string IDs
        create_student(connection, db_name, "S123", "John Doe", "john@example.com", "1995-05-20", 123456789, "password123")
        create_student(connection, db_name, "S124", "Jane Doe", "jane@example.com", "1997-07-15", 987654321, "password456")
        
        # Step 4: Fetch and print databases
        print("\nDatabases:")
        fetch_db(connection)
        
        # Step 5: Fetch and print table data
        print("\nStudent table data:")
        fetch_table(connection, db_name)
        
        # Step 6: Fetch and print a specific student by ID
        print("\nFetch student with ID S123:")
        fetch_student(connection, db_name, "S123")
        
        # Step 7: Update a student's email
        print("\nUpdate student with ID S123's email:")
        update_student(connection, db_name, "S123", "email", "john.doe@example.com")
        
        # Step 8: Fetch updated student
        print("\nFetch updated student with ID S123:")
        fetch_student(connection, db_name, "S123")
        
        # Step 9: Delete a student
        print("\nDelete student with ID S124:")
        delete_student(connection, db_name, "S124")
        
        # Step 10: Fetch and print updated table data
        print("\nUpdated student table data:")
        fetch_table(connection, db_name)
        
        # Step 11: Drop the table
        # print("\nDropping the table `students`:")
        # delete_table(connection, db_name, "students")

        # Close the connection
        connection.close()

if __name__ == "__main__":
    main()
