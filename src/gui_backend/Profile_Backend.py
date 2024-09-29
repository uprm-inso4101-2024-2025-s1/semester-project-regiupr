# fetch data and return it in an easy to access format (dictionary)
def get_student_data(fetched_student):
    characteristics = ["student_id", "name", "email", "birthdate", "ssn", "password"]
    student_data = dict(zip(characteristics, fetched_student))
    return student_data