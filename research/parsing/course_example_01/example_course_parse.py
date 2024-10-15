#from bs4 import SoupStrainer as strainer, BeautifulSoup as bsoup

from course_web_scraper import CourseWebScraper
from course_parser import CourseParser

# THIS FILE MAY BE CONVERTED TO FINAL PRODUCTION FILE ONCE ALL TODOs ARE COMPLETED


# url to download
url = 'https://www.uprm.edu/registrar/sections/index.php?v1=icom&v2=&term=2-2024&a=s&cmd1=Search'

# create new course scrapper
cws = CourseWebScraper()
#cws.set_url_to_scrap(url)
# get page content from url
page = cws.download_page_from(url)
page_content = cws.page_content()

# print results for verification
print('PAGE:\n', page)
print('CONTENT:\n', page_content)

table_id = 'results_table'

# create new course parser
cp = CourseParser()
# create parsing specifications:
# wants all tables with the specific 'table_id'
#table_spec = strainer('table', attrs={'id': table_id})
table_spec = cp.set_parsing_spec('table', 'id', table_id)

# parse only the table from page_content using
# specifications obtained with the strainer
#soup_table = bsoup(page_content, 'html.parser',
#                   parse_only=table_spec)
soup_table = cp.get_table(page_content)

print('table_spec', table_spec)
print('soup_table', soup_table)

rows = cp.get_rows(soup_table)
print('ROWS:\n', rows)

# TODO get all rows from the table
# TODO iterate through all rows, extracting each cell text according to its position
# TODO create a dictionary with data, to be done while iterating through the cells
# TODO prepare extracted data for use
