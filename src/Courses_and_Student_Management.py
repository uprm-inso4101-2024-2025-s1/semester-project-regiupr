class Student:
    # Student Constructor
    def __init__(self, student_number, email, username, ssn, password):
        # Private members
        self.student_number = student_number
        self.email = email
        self.username = username
        self.ssn = ssn
        self.password = password

    # Getters
    def get_student_number(self):
        return self.student_number

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_ssn(self):
        return self.ssn

    def get_password(self):
        return self.password

    # Setters
    def set_student_number(self, student_number):
        self.student_number = student_number

    def set_email(self, email):
        self.email = email

    def set_username(self, username):
        self.username = username

    def set_ssn(self, ssn):
        self.ssn = ssn

    def set_password(self, password):
        self.password = password
        
class Course:
     # Course Constructor
    def __init__(self, course_Initials, course_Number, course_section, isAviable):
        # Private members
        self.course_Initials = course_Initials
        self.course_Number = course_Number
        self.course_section = course_section
        self.isAviable = isAviable
        
    # Getters
    def get_course_Initials(self):
        return self.course_Initials

    def get_course_Number(self):
        return self.course_Number

    def get_course_section(self):
        return self.course_section

    def get_isAviable(self):
        return self.isAviable

    # Setters
    def set_course_Initials(self, course_Initials):
        self.course_Initials = course_Initials

    def set_course_Number(self, course_Number):
        self.course_Number = course_Number

    def set_course_section(self, course_section):
        self.course_section = course_section

    def set_isAviable(self, isAviable):
        self.isAviable = isAviable

# Examples of how to create an object and use its getters and setters:
# exampleStudent1 = Student(12345, "student@example.com", "username123", "802-24-0000", "mypassword")
# exampleStudent1.set_email("emailChanged.com")
# print(exampleStudent1.get_email())