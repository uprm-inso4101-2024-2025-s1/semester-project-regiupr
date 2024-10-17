#here we define the class SemesterPlanning which is used to store the information of a semester planning

class SemesterPlanning:
    def __init__(self, planning_id, student_id, semester_name):
        self.planning_id = planning_id
        self.student_id = student_id
        self.semester_name = semester_name

    def __repr__(self):
        return f"SemesterPlanning({self.planning_id}, {self.student_id}, {self.semester_name})"
    
def main():
    planning1 = SemesterPlanning(1, 1, "Fall 2021")
    print(planning1)

main()