import configparser
import mysql.connector
from mysql.connector import Error

    
# Establishing the connection
def create_connection():

    try:
        config = configparser.ConfigParser()
        config.read('credentials\db_config.ini')
        connection = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to create a new section
def create_section(connection, section_id, course_code, professor_name, days, schedule, room, modality, capacity):
    try:
        cursor = connection.cursor()
        sql = """
        INSERT INTO sections (section_id, course_code, professor_name, days, schedule, room, modality, capacity)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (section_id, course_code, professor_name, days, schedule, room, modality, capacity)
        cursor.execute(sql, values)
        connection.commit()
        print("Section created successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to read all sections
def read_sections(connection):
    
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM sections"
        cursor.execute(sql)
        result = cursor.fetchall()
        if (len(result)==0):
            print ("No sections found")
            return
        for row in result:
            print(row)
    except Error as e:
        print(f"Error: {e}")

# Function to update a section
def update_section(connection, section_id, professor_name=None, days=None, schedule=None, room=None, modality=None, capacity=None):
    try:
        cursor = connection.cursor()
        sql = "UPDATE sections SET "
        updates = []
        values = []


        if professor_name:
            updates.append("professor_name = %s")
            values.append(professor_name)
        if days:
            updates.append("days = %s")
            values.append(days)
        if schedule:
            updates.append("schedule = %s")
            values.append(schedule)
        if room:
            updates.append("room = %s")
            values.append(room)
        if modality:
            updates.append("modality = %s")
            values.append(modality)
        if capacity:
            updates.append("capacity = %s")
            values.append(capacity)

        if not updates:
            print("No fields to update")
            return

        sql += ", ".join(updates)
        sql += " WHERE section_id = %s"
        values.append(section_id)

        cursor.execute(sql, tuple(values))
        connection.commit()
        print("Section updated successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to delete a section
def delete_section(connection, section_id):
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM sections WHERE section_id = %s"
        cursor.execute(sql, (section_id,))
        connection.commit()
        print("Section deleted successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to select one section entry from the sections table
# and return a tuple with all the entries in the selected section for use without querying
def select_section(connection, section_id):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT * FROM sections WHERE section_id='{section_id}'")
        section = cursor.fetchone()
        if (section==None):
            return print ("Section not found")
        else:
            print(f"Section with code {section_id}: {section}")
            return section
        
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        
