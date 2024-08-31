import csv
import os
import random

def generate_class_days():
    day_map = {
        "Monday, Wednesday, Friday": "LWV",
        "Monday, Wednesday": "LW",
        "Tuesday, Thursday": "MJ",
        "Monday, Tuesday, Wednesday, Thursday": "LMWJ",
        "Friday": "V"
    }
    days = list(day_map.keys())
    return day_map[random.choice(days)]

def generate_class_hours():
    start_hour = random.randint(8, 19)  # 8am to 8pm
    start_minute = random.choice([0, 30])
    end_hour = start_hour
    end_minute = start_minute + 50
    if end_minute >= 60:
        end_minute -= 60
        end_hour += 1
    if end_hour > 19:  # Ensure it does not go past 8pm
        end_hour = 19
        end_minute = 0

    # Convert to 12-hour format
    start_period = "AM" if start_hour < 12 else "PM"
    end_period = "AM" if end_hour < 12 else "PM"
    start_hour = start_hour if start_hour <= 12 else start_hour - 12
    end_hour = end_hour if end_hour <= 12 else end_hour - 12

    # If end hour is zero, set it to 12 (for cases like 00:30)
    end_hour = 12 if end_hour == 0 else end_hour

    return f"{start_hour}:{start_minute:02d}{start_period} - {end_hour}:{end_minute:02d}{end_period}"

def generate_sections():
    sections = []
    for _ in range(random.randint(3, 5)):
        section_code = f"0{random.randint(10, 99)}"
        class_days = generate_class_days()
        class_hours = generate_class_hours()
        available = random.choice([True, False])
        sections.append({
            "section_code": section_code,
            "days": class_days,
            "hours": class_hours,
            "available": available
        })
    return sections

def load_courses_from_csv(filepath):
    courses = []
    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            course = {
                "department": row['department'],
                "code": row['code'],
                "name": row['name'],
                "sections": generate_sections()
            }
            courses.append(course)
    return courses

def search_courses(query):
    query = query.lower()
    return [course for course in courses_data if course['code'].lower().startswith(query)]

# Path to the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), 'resources', 'CatalogoCursos.csv')

# Load courses from CSV
courses_data = load_courses_from_csv(csv_file_path)
