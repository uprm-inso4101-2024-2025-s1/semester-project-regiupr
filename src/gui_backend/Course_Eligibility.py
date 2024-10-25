import mysql.connector

class CourseEligibility:
    def __init__(self, name, code, credits, suggested_semester, can_take=False, is_taking=False):
        self.name = name
        self.code = code
        self.credits = credits
        self.suggested_semester = suggested_semester
        self.can_take = can_take
        self.is_taking = is_taking
    
    #Update whether the student can take the course.
    def update_can_take(self, status):
        self.can_take = status
    
    #Update whether the student is currently taking the course.
    def update_is_taking(self, status):
        self.is_taking = status
    
    def __repr__(self):
        return (f"('{self.name}', '{self.code}', '{self.credits}', "
                f"'{self.suggested_semester}', can_take={self.can_take}, "
                f"is_taking={self.is_taking})")
    
# Function to get the list of courses the student has not taken
def get_not_taken_courses(student_id, conn, cursor):
    # Query to get the curriculum associated with the student
    curriculum_query = """
    SELECT curriculum.curriculum_id 
    FROM student_curriculum AS sc
    JOIN curriculum ON sc.curriculum_id = curriculum.curriculum_id
    WHERE sc.student_id = %s
    """
    cursor.execute(curriculum_query, (student_id,))
    curriculum_id = cursor.fetchone()

    if not curriculum_id:
        print(f"No curriculum found for student_id {student_id}")
        return []
    
    curriculum_id = curriculum_id[0]

    # Query to get all courses in the student's curriculum that they have not taken
    uncompleted_courses_query = """
    SELECT c.course_name, c.course_code, c.credits, cc.semester 
    FROM curriculum_courses AS cc
    JOIN courses AS c ON cc.course_code = c.course_code
    LEFT JOIN student_courses AS sc ON sc.course_code = c.course_code AND sc.student_id = %s
    WHERE cc.curriculum_id = %s AND sc.course_code IS NULL
    """
    
    cursor.execute(uncompleted_courses_query, (student_id, curriculum_id))
    uncompleted_courses = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Create a list of CourseEligibility objects for uncompleted courses
    courses = []
    for course in uncompleted_courses:
        name, code, credits, suggested_semester = course
        course_obj = CourseEligibility(name=name, code=code, credits=credits, suggested_semester=suggested_semester)
        courses.append(course_obj)
    
    return courses
