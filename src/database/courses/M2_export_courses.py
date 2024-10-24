# since its not possible to run the export.py module on its current dir, I will implement it features here.

from courses import create_connection, create_course
from scrapped_curriculum.parser import course_catalog as cc

# Here some example of how section data should be organized
#
# - Cristian Marcial
dummy_data_example = {
    "INSO4101": ['080', 'INSO4101', 'Marko Schutz', 'MWF', '2:00p-3:20p', 'S113', 'Presential', '100'],
    "CIIC3015": ['133', 'CIIC3015', 'John Vasquez', 'W', '7:30a-9:20p', 'S114a', 'Presential', '50']
}

def export_courses():
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database. Exiting...")
        return

    for c in cc:
        # example: create_course(connection, 'CIIC3015', "Descripcion Nula", "Description", '3', "CIIC")
        create_course(connection, cc[0], cc[1], cc[2], cc[3], cc[4])
        print(c)
 
    connection.close()
    print("Database connection closed for sc export")

export_courses()