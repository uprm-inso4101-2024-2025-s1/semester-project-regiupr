import configparser
import mysql.connector
from mysql.connector import Error

#Variables just for reading their values
_section_id_=None
_course_id_ = None
_professor_name_ = None 
_days_ = None
_schedule_ = None
_room_ = None
_modality_ = None
_capacity_ = None

# Establishing the connection
def create_connection():
    try:
        config = configparser.ConfigParse()
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
def create_section(connection, section_id, course_id, professor_name, days, schedule, room, modality, capacity):
    try:
        cursor = connection.cursor()
        sql = """
        INSERT INTO sections (section_id, course_id, professor_name, days, schedule, room, modality, capacity)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (section_id, course_id, professor_name, days, schedule, room, modality, capacity)
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
        for row in result:
            print(row)
    except Error as e:
        print(f"Error: {e}")

# Function to update a section
def update_section(connection, section_id, course_id=None, professor_name=None, days=None, schedule=None, room=None, modality=None, capacity=None):
    try:
        cursor = connection.cursor()
        sql = "UPDATE sections SET "
        updates = []
        values = []

        if course_id:
            updates.append("course_id = %s")
            values.append(course_id)
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
# and saves values in corresponding variables
def select_sections(connection, section_id=None, course_id=None, professor_name=None, days=None, schedule=None, room=None, modality=None, capacity=None):
    try:
        cursor = connection.cursor()
        
        # Construct the SQL query dynamically based on provided parameters
        sql = "SELECT * FROM sections WHERE TRUE"
        values = []

        if section_id:
            sql += " AND section_id = %s"
            values.append(section_id)
        if course_id:
            sql += " AND course_id = %s"
            values.append(course_id)
        if professor_name:
            sql += " AND professor_name = %s"
            values.append(professor_name)
        if days:
            sql += " AND days = %s"
            values.append(days)
        if schedule:
            sql += " AND schedule = %s"
            values.append(schedule)
        if room:
            sql += " AND room = %s"
            values.append(room)
        if modality:
            sql += " AND modality = %s"
            values.append(modality)
        if capacity:
            sql += " AND capacity = %s"
            values.append(capacity)

        # Execute the query
        cursor.execute(sql, tuple(values))
        result = cursor.fetchall()
        # Saves a local copy of each value for easier access
        _section_id_ = values[0]
        _course_id_ = values[1]
        _professor_name_ = values[2] 
        _days_ = values[3]
        _schedule_ = values[4]
        _room_ = values[5]
        _modality_ = values[6]
        _capacity_ = values[7]
        
        
        # Print the results
        if result:
            for row in result:
                print(row)
            
        else:
            print("No records found")

    except Error as e:
        print(f"Error: {e}")
        