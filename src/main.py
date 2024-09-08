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

# Examples of how to create an object and use its getters and setters:
# exampleStudent1 = Student(12345, "student@example.com", "username123", "802-24-0000", "mypassword")
# exampleStudent1.set_email("emailChanged.com")
# print(exampleStudent1.get_email())
