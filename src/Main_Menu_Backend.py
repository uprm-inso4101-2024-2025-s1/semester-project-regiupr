from DB_connection import StudentsM, CoursesM, ProgramFacultyM, SectionsM, studentCoursesM

class MainMenuBackend:
    def __init__(self, student_id):
        self.connection = StudentsM.create_connection()
        self.student_id = student_id

    def fetch_student_info(self):
        student_info = StudentsM.fetch_student(self.connection, self.student_id)
        characteristics = ["student_id", "name", "email", "birthdate", "ssn", "password"]
        student_info = dict(zip(characteristics, student_info))
        return student_info
        

    def fetch_student_schedule(self):
        return SectionsM.fetch_student_schedule(self.connection, self.student_id)

    def fetch_enrolled_courses(self):
        return studentCoursesM.fetch_student_courses(self.connection, self.student_id) or []


    def fetch_professor_info(self, professor_id):
        return ProgramFacultyM.fetch_professor(self.connection, professor_id)

    def close_connection(self):
        if self.connection:
            self.connection.close()
