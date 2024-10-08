import unittest
from unittest.mock import patch, MagicMock
import mysql.connector
from students import create_connection, create_student, fetch_table, fetch_student, update_student, delete_student

class TestStudentManagement(unittest.TestCase):
    
    @patch('mysql.connector.connect')
    def test_create_connection_success(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        connection = create_connection()
        self.assertIsNotNone(connection)
        mock_connect.assert_called_once()

    @patch('mysql.connector.connect')
    def test_create_connection_failure(self, mock_connect):
        mock_connect.side_effect = mysql.connector.Error("Connection Error")
        connection = create_connection()
        self.assertIsNone(connection)

    @patch('mysql.connector.connect')
    def test_create_student(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_connect.return_value = mock_conn
        connection = create_connection()

        create_student(connection, "S001", "John Doe", "johndoe@example.com", "1998-01-15", 123456789, "password123")
        mock_cursor.execute.assert_called_with(
            "INSERT INTO students (student_id, name, email, birthdate, ssn, password) "
            "VALUES ('S001', 'John Doe', 'johndoe@example.com', '1998-01-15', 123456789, password123)"
        )
        mock_conn.commit.assert_called_once()

    @patch('mysql.connector.connect')
    def test_fetch_table(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [
            ("S001", "John Doe", "johndoe@example.com", "1998-01-15", 123456789, "password123")
        ]
        mock_connect.return_value = mock_conn
        connection = create_connection()

        rows = fetch_table(connection)
        self.assertEqual(len(rows), 1)
        mock_cursor.execute.assert_called_with("SELECT * FROM students")

    @patch('mysql.connector.connect')
    def test_fetch_student(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchone.return_value = ("S001", "John Doe", "johndoe@example.com", "1998-01-15", 123456789, "password123")
        mock_connect.return_value = mock_conn
        connection = create_connection()

        student = fetch_student(connection, "S001")
        self.assertIsNotNone(student)
        mock_cursor.execute.assert_called_with("SELECT * FROM students WHERE student_id = 'S001'")

    @patch('mysql.connector.connect')
    def test_update_student(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_connect.return_value = mock_conn
        connection = create_connection()

        update_student(connection, "S001", "email", "newemail@example.com")
        mock_cursor.execute.assert_called_with(
            "UPDATE students SET email = 'newemail@example.com' WHERE student_id = 'S001'"
        )
        mock_conn.commit.assert_called_once()

    @patch('mysql.connector.connect')
    def test_delete_student(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_connect.return_value = mock_conn
        connection = create_connection()

        delete_student(connection, "S001")
        mock_cursor.execute.assert_called_with("DELETE FROM students WHERE student_id = 'S001'")
        mock_conn.commit.assert_called_once()

if __name__ == "__main__":
    unittest.main()
