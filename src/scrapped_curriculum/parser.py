# For scrapping the src html code of the web
from requests import get
# For parsing on the web
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# This should be moved in another file as a csv and then moved here, for organization purposes 
# departments = {"CIIC": "https://www.uprm.edu/registrar/sections/index.php?v1=CIIC&v2=&term=2-2024&a=s&cmd1=Search",
#                "ADMI": "https://www.uprm.edu/registrar/sections/index.php?v1=ADMI&v2=&term=2-2024&a=s&cmd1=Search",
#                "ESPA": "https://www.uprm.edu/registrar/sections/index.php?v1=ESPA&v2=&term=2-2024&a=s&cmd1=Search"}

departments = {
                "ESPA": "https://www.uprm.edu/registrar/sections/index.php?v1=ESPA&v2=&term=2-2024&a=s&cmd1=Search"}           
section_catalog = {}
course_catalog = {}

for k in departments:
    page = get(departments[k])

    # parse table by id
    table_id = 'results_table'
    only_table_id = SoupStrainer('table', attrs={'id': table_id})
    soup_table = BeautifulSoup(page.content, 'html.parser', parse_only=only_table_id)

    # get rows from table
    rows_table = []
    cols_row = []
    row_data = []

    for row in soup_table.find_all('tr'):
        rows_table.append(row)
            
    for col in rows_table:
        for cell in col.find_all('td'):
            row_data.append(cell.text)

    # Example:
    # create_section(connection, section_id, course_id, professor_name, days, schedule, room, modality, capacity)
    # sections.create_section(conn, '080', 'INSO4101', 'Marko Schutz', 'MWF', '2:00p-3:20p', 'S113', 'Presential', '100')
    row_data = list(filter(None, row_data))

    for i in range(0, len(row_data), 7):
        course_name = row_data[i+1].rsplit("-", 1)

        modality = 'Presential'
        if (len(course_name[1][:3]) > 3):
            if course_name[1][3] == 'D':
                modality = 'Asynchronous'
            elif course_name[1][3] == 'E':
                modality = 'Synchronous'

        # 0: schedule, 1: days, 3: room
        if '\xa0' not in row_data[i+4]:
            i+=1
            break
        schelude = row_data[i+4].split('\xa0')
        if len(schelude[3]) == 0:
            schelude[3] = 'nulo'

        elm = [
            course_name[1][:3], # section
            course_name[0][-8:], # course id
            row_data[i+5], # profesor name
            schelude[1].strip(), # days
            schelude[0], # schedule
            schelude[3], # room
            modality, # it speaks by itself
            50 # capacity (50 by default for now)
        ]
        section_catalog[course_name[0][-8:] + "-" + course_name[1]] = elm

        # example: create_course(connection, 'CIIC3015', "Introduction to Computer Programming I", "Description", '3', "CIIC")
        if course_name[0][-8:] not in course_catalog:
            course_catalog[course_name[0][-8:]] = [course_name[0][-8:], course_name[0][:-8], "Descripcion Nula",  row_data[i+2], course_name[0][-8:-4]]

for k in course_catalog:
    print(k, course_catalog[k])