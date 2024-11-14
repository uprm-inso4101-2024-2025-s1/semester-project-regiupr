#here we define the class SemesterPlanning which is used to store the information of a semester planning

from Course_Eligibility import CourseEligibility

class SemesterPlanning:
    def __init__(self, planning_id, student_id, semester_name, courses=None):
        self.planning_id = planning_id
        self.student_id = student_id
        self.semester_name = semester_name
        self.courses = courses if courses is not None else []

    def __repr__(self):
        return f"SemesterPlanning({self.planning_id}, {self.student_id}, {self.semester_name}, Courses: {self.courses})"
    
def main():
    c1=CourseEligibility("Introduction to Software Engineering", "ININ4010", 3, 5)
    c2=CourseEligibility("Introduction to Software Engineering", "ININ4010", 3, 5)
    s1=[c1,c2]
    planning1 = SemesterPlanning(1, 1, "Fall 2021",s1)
    print(planning1)

if __name__ == "__main__":
    main()