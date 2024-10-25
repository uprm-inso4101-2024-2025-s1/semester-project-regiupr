# since its not possible to run the export.py module on its current dir, I will implement it features here.

from courses import create_connection, create_course
from parser_c import get_course_catalog

# Here some example of how section data should be organized
#
# - Cristian Marcial
dummy_data_example = {
    "INSO4101": ['080', 'INSO4101', 'Marko Schutz', 'MWF', '2:00p-3:20p', 'S113', 'Presential', '100'],
    "CIIC3015": ['133', 'CIIC3015', 'John Vasquez', 'W', '7:30a-9:20p', 'S114a', 'Presential', '50']
}
cc = get_course_catalog().values()

def export_courses():
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database. Exiting...")
        return
    
    for c in cc:
        # example: create_course(connection, 'CIIC3015', "Descripcion Nula", "Description", '3', "CIIC")
        create_course(connection, c[0], c[1], c[2], c[3], c[4])
        print(c)
 
    connection.close()
    print("Database connection closed for sc export")

export_courses()

# for k in cc:
#      print(k[0], k[1])