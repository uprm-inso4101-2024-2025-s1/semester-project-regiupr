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

# Testing the class
if __name__ == "__main__":
    # Create a course eligibility object
    course1 = CourseEligibility(name="Introduction to Software Engineering", code="ININ4010", credits=3, suggested_semester=5)
    
    print(course1)  # Output: CourseEligibility(name='Introduction to Software Engineering', code='ININ4010', credits=3, suggested_semester=5, can_take=False, is_taking=False)
    
    #Update can_take and is_taking status
    course1.update_can_take(True)
    course1.update_is_taking(True)

    print(course1)  # Output: ('Introduction to Software Engineering', 'ININ4010', '3', '5', can_take=True, is_taking=True)
