# Import from locally created modules
from course_web_scraper import CourseWebScraper
from course_parser import CourseParser

# URL to download (CURRENT: ICOM, 2024_S2)
url = 'https://www.uprm.edu/registrar/sections/index.php?v1=icom&v2=&term=2-2024&a=s&cmd1=Search'

# Create a new course scrapper as 'cws'
cws = CourseWebScraper()
# Download the web page from URL, save to 'page'
page = cws.download_page_from(url)
# Extract content from downloaded page, save to 'page_content'
page_content = cws.page_content()

##=========================================================
print('=========================================================')
# Print 'page'
print('PAGE:\ttype: ', type(page), '\n', page)
# Print 'page_content'
print('PAGE_CONTENT:\tlenght: ', len(page_content),
      'type: ', type(page_content), '\n', page_content)
print('=========================================================')
##=========================================================

# Tag and attribute of interest
tag, tag_attr = 'table', 'id'
# Value of id of interest
table_id = 'results_table'

# Create a new course parser as 'cp'
cp = CourseParser()
# Use strainer to get specification of tag of interest
table_spec = cp.strainer(tag, tag_attr, table_id)
# Parse the 'page_content'; the parser already knows what to parse
soup_table = cp.get_table_from(page_content)


##=========================================================
print('=========================================================')
# Print strained 'table_spec'
print('table_spec:\tlenght: ', 'type: ', type(table_spec),
      '\n', table_spec)
print('=========================================================')
# Print 'soup_table'
#print('soup_table:\tlenght: ', len(soup_table),
#      'type: ', type(soup_table), '\n', soup_table)
print('=========================================================')
##=========================================================


# Empty list of rows
row_list = []

# Extract all rows from the table
table_rows = cp.get_rows_from(soup_table)

##=========================================================
print('table_rows:\tlenght: ', len(table_rows),
      'type: ', type(table_rows), '\n', table_rows, type(table_rows[0]))
##=========================================================


# Empty list of columns
col_list = []
# Empty dictionary of colums
col_dict = {}

print('=========================================================')
print('=========================================================')
row_content = []
#for row in table_rows:
row_content = table_rows[0].find_all('th')
print(row_content)
print(len(row_content))
col_dict = {
        "Course"        : row_content[1].text,
        "Credits"       : row_content[2].text,
        "Meetings"      : row_content[4].text,
        "Professor(s)"  : row_content[5].text
        }
print(col_dict)

row_content = table_rows[1].find_all('td')
print(row_content)
print(len(row_content))
col_dict = {
        "Course"        : row_content[1].text,
        "Credits"       : row_content[2].text,
        "Meetings"      : row_content[4].text,
        "Professor(s)"  : row_content[5].text
        }
print(col_dict)
