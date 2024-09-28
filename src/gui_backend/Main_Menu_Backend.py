from DB_connection import StudentsM, ProgramFacultyM, SectionsM, studentCoursesM

class MainMenuBackend:
    def __init__(self, student_id):
        self.connection = StudentsM.create_connection()
        self.student_id = student_id

    def fetch_student_info(self):
        return StudentsM.fetch_student(self.connection, self.student_id)

    # def fetch_student_schedule(self):
    #     pass
    #     #return SectionsM.fetch_student_schedule(self.connection, self.student_id)

    def fetch_enrolled_courses(self):
        return studentCoursesM.fetch_student_courses(self.connection, self.student_id) or []

    # def fetch_professor_info(self, professor_id):
    #     pass
    #     #return ProgramFacultyM.fetch_professor(self.connection, professor_id)

    def close_connection(self):
        if self.connection:
            self.connection.close()