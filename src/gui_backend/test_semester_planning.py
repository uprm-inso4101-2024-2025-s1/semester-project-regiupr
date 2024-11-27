import unittest
from unittest.mock import MagicMock, patch
from SemesterPlanning import SemesterPlanning
from Course_Eligibility import CourseEligibility

# This class is used to create unit tests for the SemesterPlanning class
class TestSemesterPlanning(unittest.TestCase):
    def setUp(self):
        # Set up a mock database connection and mock cursor to simulate interactions with the database
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value.__enter__.return_value = self.mock_cursor

        # Sample data for courses used in the tests
        self.c1 = CourseEligibility("Computer Networks", "CIIC4070", 3, 8)
        self.c2 = CourseEligibility("Computer Architecture", "CIIC4082", 3, 6)
        self.planned_courses = [self.c1, self.c2]

        # Create an instance of SemesterPlanning to be used in the tests
        self.semester_planning = SemesterPlanning(1, "S004", "Fall 2021", self.planned_courses)

    def test_read_by_id(self):
        # Test the read_by_id method to ensure it retrieves the correct semester planning from the database
        self.mock_cursor.fetchone.return_value = (1, "S004", "Fall 2021")
        self.mock_cursor.fetchall.return_value = [
            ("CIIC4070", "Computer Networks", 3),
            ("CIIC4082", "Computer Architecture", 3)
        ]

        result, courses = SemesterPlanning.read_by_id(self.mock_conn, 1)
        self.assertEqual(result, (1, "S004", "Fall 2021"))
        self.assertEqual(len(courses), 2)

    def test_insert_course(self):
        # Test the insert_course method to ensure a new course is added to the semester planning
        new_course = CourseEligibility("Data Structures", "CIIC4020", 4, 3)
        self.semester_planning.insert_course(self.mock_conn, new_course)
        self.assertIn(new_course, self.semester_planning.planned_courses)
        self.assertGreaterEqual(self.mock_conn.commit.call_count, 1)

    def test_update_course(self):
        # Test the update_course method to ensure an existing course is updated correctly in the semester planning
        updated_course = CourseEligibility("Advanced Networks", "CIIC4070", 3, 9)
        self.semester_planning.update_course(self.mock_conn, "CIIC4070", updated_course)
        self.assertIn(updated_course, self.semester_planning.planned_courses)
        self.assertGreaterEqual(self.mock_conn.commit.call_count, 1)

    def test_delete_course(self):
        # Test the delete_course method to ensure a course is removed from the semester planning
        self.semester_planning.delete_course(self.mock_conn, "CIIC4070")
        self.assertNotIn(self.c1, self.semester_planning.planned_courses)
        self.assertGreaterEqual(self.mock_conn.commit.call_count, 1)

    def test_delete(self):
        # Test the delete method to ensure a semester planning and its associated courses are deleted from the database
        SemesterPlanning.delete(self.mock_conn, 1)
        self.mock_cursor.execute.assert_any_call("DELETE FROM planned_courses WHERE planning_id = %s", (self.semester_planning.planning_id,))
        self.mock_cursor.execute.assert_any_call("DELETE FROM semester_planning WHERE planning_id = %s", (self.semester_planning.planning_id,))
        self.assertGreaterEqual(self.mock_conn.commit.call_count, 1)

if __name__ == "__main__":
    unittest.main()
