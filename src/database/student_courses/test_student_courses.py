import unittest
from unittest.mock import patch, MagicMock
from student_courses import create_connection, create_student_course, fetch_table, fetch_student_courses, update_student_course, delete_student_course

class TestStudentCourses(unittest.TestCase):

    @patch('mysql.connector.connect')
    def test_create_connection_success(self, mock_connect):
        # Mock the connection object
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        connection = create_connection()
        
        # Assert that the connection was successful
        self.assertIsNotNone(connection)
        mock_connect.assert_called_once()

    @patch('mysql.connector.connect')
    def test_create_student_course(self, mock_connect):
        # Mock connection and cursor
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_connect.return_value = mock_conn

        connection = create_connection()
        create_student_course(connection, 'S001', 'CS101', 'A', 'Enrolled')
        
        # Check if the correct query was executed
        mock_cursor.execute.assert_called_with(
            "INSERT INTO student_courses (student_id, course_code, section_id, status) VALUES ('S001', 'CS101', 'A', 'Enrolled')"
        )
        mock_conn.commit.assert_called_once()

    @patch('mysql.connector.connect')
    def test_fetch_table(self, mock_connect):
        # Mock connection and cursor
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [
            ('S001', 'CS101', 'A', 'Enrolled'),
            ('S002', 'CS103', 'C', 'Completed')
        ]
        mock_connect.return_value = mock_conn

        connection = create_connection()
        fetch_table(connection)
        
        # Check if the correct query was executed
        mock_cursor.execute.assert_called_with("SELECT * FROM student_courses")
        self.assertEqual(mock_cursor.fetchall.call_count, 1)

    @patch('mysql.connector.connect')
    def test_fetch_student_courses(self, mock_connect):
        # Mock connection and cursor
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [
            ('S001', 'CS101', 'A', 'Enrolled'),
            ('S001', 'CS102', 'B', 'Enrolled')
        ]
        mock_connect.return_value = mock_conn

        connection = create_connection()
        fetch_student_courses(connection, 'S001')
        
        # Check if the correct query was executed
        mock_cursor.execute.assert_called_with("SELECT * FROM student_courses WHERE student_id='S001'")
        self.assertEqual(mock_cursor.fetchall.call_count, 1)

    @patch('mysql.connector.connect')
    def test_update_student_course(self, mock_connect):
        # Mock connection and cursor
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_connect.return_value = mock_conn

        connection = create_connection()
        update_student_course(connection, 'S001', 'CS101', 'status', 'Completed')
        
        # Check if the correct update query was executed
        mock_cursor.execute.assert_called_with(
            "UPDATE student_courses SET status = 'Completed' WHERE student_id = 'S001' AND course_code = 'CS101'"
        )
        mock_conn.commit.assert_called_once()

    @patch('mysql.connector.connect')
    def test_delete_student_course(self, mock_connect):
        # Mock connection and cursor
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_connect.return_value = mock_conn

        connection = create_connection()
        delete_student_course(connection, 'S001', 'CS101')
        
        # Check if the correct delete query was executed
        mock_cursor.execute.assert_called_with(
            "DELETE FROM student_courses WHERE student_id = 'S001' AND course_code = 'CS101'"
        )
        mock_conn.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
