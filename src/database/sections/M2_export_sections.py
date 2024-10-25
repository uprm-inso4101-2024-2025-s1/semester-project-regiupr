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
sc = get_section_catalog()

def export_sections():
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database. Exiting...")
        return

    for s in sc:
        create_section(connection, sc[0], sc[1], sc[2], sc[3], sc[4], sc[5], sc[6], sc[7])
        print(s)
 
    connection.close()
    print("Database connection closed for sc export")

export_sections()