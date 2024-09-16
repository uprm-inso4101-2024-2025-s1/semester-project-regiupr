from database.students import create_student, fetch_student, update_student, delete_student
from database.student_courses import create_student_course, fetch_student_courses, update_student_course, delete_student_course
from database.courses import create_course, fetch_course, update_course, delete_course, create_connection
from database.sections import create_section, read_sections, update_section, delete_section, select_sections
from database.program_faculty import create_program_faculty, fetch_program_faculty, update_program_faculty, delete_program_faculty

class Student:
    def __init__(self, student_number, email, username, ssn, password):
        self.student_number = student_number
        self.email = email
        self.username = username
        self.ssn = ssn
        self.password = password

    def save_to_db(self):
        connection = create_connection()
        if connection:
            create_student(connection, self.student_number, self.username, self.email, '1990-01-01', self.ssn, self.password)
            connection.close()

    def update_in_db(self, field, value):
        connection = create_connection()
        if connection:
            update_student(connection, self.student_number, field, value)
            connection.close()

    @classmethod
    def fetch_from_db(cls, student_number):
        connection = create_connection()
        if connection:
            student_data = fetch_student(connection, student_number)
            connection.close()
            if student_data:
                return cls(*student_data)
        return None

    def delete_from_db(self):
        connection = create_connection()
        if connection:
            delete_student(connection, self.student_number)
            connection.close()

# Example of use:
# student1 = Student("S004", "email@example.com", "new_user", "123456789", "password")
# student1.save_to_db()

class Student_Courses:
    def __init__(self, student_id, course_code, section_id, status):
        self.student_id = student_id
        self.course_code = course_code
        self.section_id = section_id
        self.status = status

    def save_to_db(self):
        connection = create_connection()
        if connection:
            create_student_course(connection, self.student_id, self.course_code, self.section_id, self.status)
            connection.close()

    def update_in_db(self, field, value):
        connection = create_connection()
        if connection:
            update_student_course(connection, self.student_id, self.course_code, field, value)
            connection.close()

    @classmethod
    def fetch_from_db(cls, student_id):
        connection = create_connection()
        if connection:
            student_courses = fetch_student_courses(connection, student_id)
            connection.close()
            return [cls(*course) for course in student_courses]
        return []

    def delete_from_db(self):
        connection = create_connection()
        if connection:
            delete_student_course(connection, self.student_id, self.course_code)
            connection.close()

# Example of use:
# student_course = Student_Courses("S001", "CS105", "A", "Enrolled")
# student_course.save_to_db()

class Course:
    def __init__(self, course_code, course_name, description, credits, program):
        self.course_code = course_code
        self.course_name = course_name
        self.description = description
        self.credits = credits
        self.program = program
        self.faculty = None
        self.sections = []

    def save_to_db(self):
        connection = create_connection()
        if connection:
            create_course(connection, self.course_code, self.course_name, self.description, self.credits, self.program)
            connection.close()

    def update_in_db(self, field, value):
        connection = create_connection()
        if connection:
            update_course(connection, self.course_code, field, value)
            connection.close()

    @classmethod
    def fetch_from_db(cls, course_code):
        connection = create_connection()
        if connection:
            course_data = fetch_course(connection, course_code)
            connection.close()
            if course_data:
                return cls(*course_data)
        return None

    def delete_from_db(self):
        connection = create_connection()
        if connection:
            delete_course(connection, self.course_code)
            connection.close()

    def add_section(self, section_id, professor_name, days, schedule, room, modality, capacity):
        connection = create_connection()
        if connection:
            create_section(connection, section_id, self.course_code, professor_name, days, schedule, room, modality, capacity)
            connection.close()
            self.sections.append({
                "section_id": section_id,
                "professor_name": professor_name,
                "days": days,
                "schedule": schedule,
                "room": room,
                "modality": modality,
                "capacity": capacity
            })

    def update_section(self, section_id, field, value):
        connection = create_connection()
        if connection:
            update_section(connection, section_id, **{field: value})
            connection.close()

    def delete_section(self, section_id):
        connection = create_connection()
        if connection:
            delete_section(connection, section_id)
            connection.close()
            self.sections = [sec for sec in self.sections if sec["section_id"] != section_id]

    def fetch_sections(self):
        connection = create_connection()
        if connection:
            self.sections = select_sections(connection, course_id=self.course_code)
            connection.close()
        return self.sections

    def add_faculty(self, faculty):
        connection = create_connection()
        if connection:
            create_program_faculty(connection, self.program, faculty)
            connection.close()
            self.faculty = faculty

    def fetch_faculty(self):
        connection = create_connection()
        if connection:
            faculty_data = fetch_program_faculty(connection, self.program)
            connection.close()
            if faculty_data:
                self.faculty = faculty_data[1]
            return self.faculty

    def update_faculty(self, new_faculty):
        connection = create_connection()
        if connection:
            update_program_faculty(connection, self.program, 'faculty', new_faculty)
            connection.close()
            self.faculty = new_faculty

    def delete_faculty(self):
        connection = create_connection()
        if connection:
            delete_program_faculty(connection, self.program)
            connection.close()
            self.faculty = None

# Example of use:
# course = Course('CIIC3015', 'Introduction to Computer Programming', 'Learning programming', 3, 'CIIC')
# course.save_to_db()
