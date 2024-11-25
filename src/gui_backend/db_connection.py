import mysql.connector
from mysql.connector import Error
import configparser

# Establishing the connection
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
            print("Connection to MySQL DB successful")
            return connection
    except configparser.NoSectionError:
        print("Error: Missing [mysql] section in db_config.ini.")
    except configparser.NoOptionError as e:
        print(f"Error: Missing option in db_config.ini: {e}")
    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None