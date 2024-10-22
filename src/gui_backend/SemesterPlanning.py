#here we define the class SemesterPlanning which is used to store the information of a semester planning

from Course_Eligibility import CourseEligibility
from db_connection import create_connection

class SemesterPlanning:
    def __init__(self, planning_id, student_id, semester_name, courses=None):
        self.planning_id = planning_id
        self.student_id = student_id
        self.semester_name = semester_name
        self.planned_courses = courses if courses is not None else []

    def __repr__(self):
        return f"SemesterPlanning({self.planning_id}, {self.student_id}, {self.semester_name}, Courses: {self.planned_courses})"
    
    # Helper method to insert courses into the planned_courses table
    def _insert_courses(self, conn):
        try:
            with conn.cursor() as cursor:
                sql = """
                INSERT INTO planned_courses (planning_id, course_code)
                VALUES (%s, %s)
                """
                for course in self.planned_courses:
                    cursor.execute(sql, (self.planning_id, course.code))  # Use course code to link
                conn.commit()
                print(f"Courses for SemesterPlanning {self.planning_id} added successfully.")
        except Exception as e:
            conn.rollback()
            print(f"Error inserting courses: {e}")

    # Create a new semester planning and associated courses
    def create(self, conn):
        try:
            conn.autocommit = False
            with conn.cursor() as cursor:
                sql = """
                INSERT INTO semester_planning (planning_id, student_id, semester_name)
                VALUES (%s, %s, %s)
                """
                cursor.execute(sql, (self.planning_id, self.student_id, self.semester_name))
                self._insert_courses(conn)  # Insert the courses associated with this planning
                conn.commit()
                print(f"SemesterPlanning {self.planning_id} created successfully.")
        except Exception as e:
            conn.rollback()
            print(f"Error creating SemesterPlanning: {e}")
        finally:
            conn.autocommit = True

    # Read semester planning by planning_id, including courses
    @staticmethod
    def read_by_id(conn, planning_id):
        try:
            with conn.cursor() as cursor:
                # Read semester planning details
                sql = "SELECT * FROM semester_planning WHERE planning_id = %s"
                cursor.execute(sql, (planning_id,))
                result = cursor.fetchone()

                if result:
                    # Read associated courses, join with courses table for more details
                    sql_courses = """
                    SELECT c.course_code, c.course_name, c.credits 
                    FROM planned_courses pc
                    JOIN courses c ON pc.course_code = c.course_code
                    WHERE pc.planning_id = %s
                    """
                    cursor.execute(sql_courses, (planning_id,))
                    courses = cursor.fetchall()
                    print(f"SemesterPlanning found: {result}, Courses: {courses}")
                    return result, courses
                else:
                    print(f"No SemesterPlanning found with ID {planning_id}")
        except Exception as e:
            print(f"Error reading SemesterPlanning: {e}")

    # Update an existing semester planning and its courses
    def update(self, conn):
        try:
            conn.autocommit = False
            with conn.cursor() as cursor:
                sql = """
                UPDATE semester_planning
                SET student_id = %s, semester_name = %s
                WHERE planning_id = %s
                """
                cursor.execute(sql, (self.student_id, self.semester_name, self.planning_id))
                
                # Delete existing planned courses and insert the updated list
                sql_delete_courses = "DELETE FROM planned_courses WHERE planning_id = %s"
                cursor.execute(sql_delete_courses, (self.planning_id,))
                self._insert_courses(conn)  # Re-insert updated courses
                
                conn.commit()
                print(f"SemesterPlanning {self.planning_id} updated successfully.")
        except Exception as e:
            conn.rollback()
            print(f"Error updating SemesterPlanning: {e}")
        finally:
            conn.autocommit = True

    # Delete semester planning and its associated courses
    @staticmethod
    def delete(conn, planning_id):
        try:
            conn.autocommit = False
            with conn.cursor() as cursor:
                # Delete associated planned_courses first (cascade)
                sql_courses = "DELETE FROM planned_courses WHERE planning_id = %s"
                cursor.execute(sql_courses, (planning_id,))
                
                # Delete the semester planning
                sql = "DELETE FROM semester_planning WHERE planning_id = %s"
                cursor.execute(sql, (planning_id,))
                
                conn.commit()
                print(f"SemesterPlanning {planning_id} and associated planned courses deleted successfully.")
        except Exception as e:
            conn.rollback()
            print(f"Error deleting SemesterPlanning: {e}")
        finally:
            conn.autocommit = True

def main():
    conn = create_connection()  # Database connection

    # Example usage of the CRUD functions
    c1 = CourseEligibility("Computer Networks", "CIIC4070", 3, 8)
    c2 = CourseEligibility("Computer Architecture", "CIIC4082", 3, 6)
    c3= CourseEligibility("Data Structures","CIIC4020",4,3)
    c4= CourseEligibility("Foundations of Computing","CIIC3075",3,2)
    planned_courses = [c1, c2]
    updated_courses=[c3,c4]


    # Create instance of SemesterPlanning
    planning1 = SemesterPlanning(1, "S004", "Fall 2021", planned_courses)

    # Create a new semester planning in the database
    planning1.create(conn)

    # Read semester planning by planning_id
    SemesterPlanning.read_by_id(conn, 1)

    # Update semester planning name and courses
    planning1.semester_name = "Spring 2022"
    planning1.planned_courses=updated_courses

    planning1.update(conn)

    # Delete semester planning
    SemesterPlanning.delete(conn, 1)

    conn.close()  # Close the db connection

if __name__ == "__main__":
    main()