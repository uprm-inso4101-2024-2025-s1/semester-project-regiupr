import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))

import database.courses.courses as CoursesM
import database.program_faculty.program_faculty as ProgramFacultyM
import database.sections.sections as SectionsM
import database.student_courses.student_courses as studentCoursesM
import database.students.students as StudentsM

#cc.main()