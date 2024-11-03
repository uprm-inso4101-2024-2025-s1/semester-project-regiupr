# since its not possible to run the export.py module on its current dir, I will implement it features here.

from sections import create_connection, create_section
from parser_s import get_section_catalog

# Here some example of how section data should be organized
#
# - Cristian Marcial
dummy_data_example = {
    "INSO4101": ['080', 'INSO4101', 'Marko Schutz', 'MWF', '2:00p-3:20p', 'S113', 'Presential', '100'],
    "CIIC3015": ['133', 'CIIC3015', 'John Vasquez', 'W', '7:30a-9:20p', 'S114a', 'Presential', '50']
}
sc = get_section_catalog().values()

def export_sections():
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database. Exiting...")
        return

    for s in sc:
        print(s[1])
        create_section(connection, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7])
 
    connection.close()
    print("Database connection closed for sc export")

export_sections()