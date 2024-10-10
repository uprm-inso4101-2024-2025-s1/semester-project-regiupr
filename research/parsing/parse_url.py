import requests
from bs4 import SoupStrainer as strainer
from bs4 import BeautifulSoup as soup

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

# parse tables only
##only_table_tags = strainer('table')
##table_soup = soup(page_content, 'html.parser', parse_only=only_table_tags)
##print('only_table_tags\n', table_soup)
##print(only_table_tags)

# parse table by id
only_table_id = strainer('table', attrs={'id': table_id})
table_id_soup = soup(page_content, 'html.parser', parse_only=only_table_id)
print(only_table_id)
print('only_table_tags\n', table_id_soup)
