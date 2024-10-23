from DB_connection import CoursesM
from parser import section_catalog as sc

# Dummy Data
dummy_data = {
    "SEC050": {
        "course_code": "CIIC3015",
        "professor": "ALFREDO SOTO VELEZ",
       "schedule": "W 11:30 am - 1:20 pm",
       "room": "S 114a",
        "modality": "In-person",
        "capacity": 25
    },
    "SEC030L": {
        "course_code": "CIIC4020",
        "professor": "JOSE QUINONES VELEZ",
        "schedule": "L 9:30 am - 11:20 am",
        "room": "S 114a",
        "modality": "In-person",
        "capacity": 20
    }
}

# Here some example of how section data should be organized
#
# - Cristian Marcial
dummy_data_example = {
    "INSO4101": ['080', 'INSO4101', 'Marko Schutz', 'MWF', '2:00p-3:20p', 'S113', 'Presential', '100'],
    "CIIC3015": ['133', 'CIIC3015', 'John Vasquez', 'W', '7:30a-9:20p', 'S114a', 'Presential', '50']
}

def export_sections():
    connection = CoursesM.create_connection()
    if connection is None:
        print("Failed to connect to the database. Exiting...")
        return

    for section_id, section_info in dummy_data.items():
        course_id = section_info["course_code"]
        professor_name = section_info["professor"]
        days = section_info["schedule"].split(" ")[0]  
        schedule = section_info["schedule"].split(" ")[1] 
        room = section_info["room"]
        modality = section_info["modality"]
        capacity = section_info["capacity"]

        try:
            CoursesM.create_course(connection, section_id, course_id, professor_name, days, schedule, room, modality, capacity)
            print(f"Exported section {section_id} for course {course_id}.")
        except Exception as e:
            print(f"Failed to export section {section_id}: {e}")
            
    connection.close()
    print("Database connection closed.")


def divide_sections() :
    #added data dictionary
    data_courses = sc
    divided_data = []
    for course_info in data_courses:
        for element in course_info:
            code = element[0]
            courses_id = element[1]
            prof = element[2]
            course_days = element[3]
            schedule = element[4]
            room = element[5]
            mod = element[6]
            max_cap = element[7]
        divided_data.append(element)
        
    CoursesM.create_course(CoursesM.create_connection(), code, courses_id, prof, course_days, schedule, room, mod, max_cap)
    return divided_data
    
if __name__ == "__main__":
    export_sections()
