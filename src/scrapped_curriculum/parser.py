# For scrapping the src html code of the web
from requests import get
# For parsing on the web
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# This should be moved in another file as a csv and then moved here, for organization purposes 
departments = {"CIIC": "https://www.uprm.edu/registrar/sections/index.php?v1=CIIC&v2=&term=2-2024&a=s&cmd1=Search",
               "ADMI": "https://www.uprm.edu/registrar/sections/index.php?v1=ADMI&v2=&term=2-2024&a=s&cmd1=Search",
               "ESPA": "https://www.uprm.edu/registrar/sections/index.php?v1=ESPA&v2=&term=2-2024&a=s&cmd1=Search",
               "INSO": "https://www.uprm.edu/registrar/sections/index.php?v1=inso&v2=&term=2-2024&a=s&cmd1=Search"}
               
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

    # Example
    # create_section(connection, section_id, course_id, professor_name, days, schedule, room, modality, capacity)
    # sections.create_section(conn, '080', 'INSO4101', 'Marko Schutz', 'MWF', '2:00p-3:20p', 'S113', 'Presential', '100')
    row_data = list(filter(None, row_data))

    for i in range(0, len(row_data), 7):
        course_name = row_data[i+1].rsplit("-", 1)
        #print(course_name)

        modality = 'Presential'
        if (len(course_name[1][:3])>3):
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
            row_data[i+5], #profesor name
            schelude[1], # days
            schelude[0], # shcedule
            schelude[3], # room
            modality, # it speaks by itself
            50 # capacity (50 by default for now)
        ]
        section_catalog[course_name[0][-8:] + "-" + course_name[1]] = elm
    print(section_catalog)

# print(uprm_page.text)

# we iterate only one time but we scrap the title alone and
# for k in departments:
#   uprm_page = get(departments[k])
#   #token_list = parser(uprm_page.text, "html.parser")
#   print()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# outputs for the export module:
# section_catalog = {"course4101-101": ["depto", "professor, "etc]}
# course_catalog = {"course": ["etc"]}
#section_catalog = {}
#course_catalog = {}

# this scraps the page
#uprm_page = get(departments["CIIC"])

#scrapped_page = BeautifulSoup(uprm_page.text, "html.parser")
#catalog_1 = scrapped_page.findAll("table", attrs={"class":"section_results"})
#soup2 = BeautifulSoup('\n'.join(map(str, catalog_1)))


#print(catalog_1[0]) # the course 
#print((catalog_1[0]))