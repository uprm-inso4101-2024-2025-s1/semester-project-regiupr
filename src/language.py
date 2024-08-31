import csv
# ---
# NOTE: 
# - The words and sentences should be stored apropietly in a csv 
# or txt file and not loaded in a list.
#
# - This module should be in another folder diferent from 'src', but 
# that will require further work with os.path
# ---



# ENGLISH
en_display_results = ["Sections:", "Department: ", "More Details", "Enroll"]
en_show_details = ["Details for "]
en_show_sections = ["Select Section for ", "Section: ", "Days: ", "Hours: ", "Available", "Not Available", "Availability: ", "Enroll"]
en_enroll_section = ["Enroll", "Do you want to enroll in Section ", "for", "?", "Enrollment", "Enrolled in Section", "of", "Section ", "is not available for enrollment."]
en_show_enrolled_courses = ["Enrolled Courses"]
en_headers = ["Course Code", "Course Name", "Section", "Class Days", "Class Hours"]
en_on_search = ["No courses found. Please make sure you are entering a valid course code."]
en_other = ["Insert Course Code Below. Ex: ICOM4009"]
txt_doc_EN = []

#SPANISH
txt_doc_ES = []


def selected_language(lang_id):
    match lang_id:
        case 1:
            return txt_doc_EN
        case 2:
            return txt_doc_ES