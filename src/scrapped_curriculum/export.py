from DB_connection import CoursesM


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
            CoursesM.create_section(connection, section_id, course_id, professor_name, days, schedule, room, modality, capacity)
            print(f"Exported section {section_id} for course {course_id}.")
        except Exception as e:
            print(f"Failed to export section {section_id}: {e}")


    connection.close()
    print("Database connection closed.")

if __name__ == "__main__":
    export_sections()
