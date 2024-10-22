import requests
from bs4 import SoupStrainer as strainer
from bs4 import BeautifulSoup as bsoup

url_icom = 'https://www.uprm.edu/registrar/sections/index.php?v1=icom&v2=&term=2-2024&a=s&cmd1=Search'
page = requests.get(url_icom)

if page.status_code == 200:
    print(page.status_code, '==> Success: page extracted')
else:
    print('Failed to read url')

# attributes of table of interest
table_class = 'section_results'
table_id = 'results_table'

page_content = page.content

# parse table by id
only_table_id = strainer('table', attrs={'id': table_id})
soup_table = bsoup(
    page_content,
    'html.parser',
    parse_only=only_table_id)
# print(only_table_id)
# print('soup_table:\n', soup_table)

# get rows from table
rows_table = []
row_data = []
cols_row = []

row_number = 0
cell_number = 0

for row in soup_table.find_all('tr'):
    rows_table.append(row)
#     print(row.text)
    for col in row:
        cols_row.append(col)
        
for col in rows_table:
    for cell in col.find_all('td'):
#         print(type(cell), len(cell))
        row_data.append(cell.text)


#print(soup_table) # single table from html page, 1 element (table)
#print(rows_table) # rows from table, 85 elements (rows)
#print(cols_row)   # cols from row, 342 elements (cols)
#print(row_data)   # text data from col, 336 elements (data)
                  # header data (<th></th>) not included
#print(len(soup_table), len(rows_table), len(cols_row), len(row_data))
# print('rows_table:\n', rows_table)

#=====================================================================
# NEW TESTING

# get rows only faster
rows_all = soup_table.find_all('tr')
#print('all rows only:')
#print(rows_all)

# get a list of columns of each row, as a list
row_cols = []
for row in rows_all:
    row_cols.append(row.find_all('td'))
print(row_cols)