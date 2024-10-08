# For scrapping the src html code of the web
from requests import get
# For parsing on the web
from bs4 import BeautifulSoup as parse_page
# 
import csv

# This should be moved in another file as a csv and then moved here, for organization purposes 
departments = {"CIIC": "https://www.uprm.edu/registrar/sections/index.php?v1=CIIC&v2=&term=2-2024&a=s&cmd1=Search",
               "ADMI": "https://www.uprm.edu/registrar/sections/index.php?v1=ADMI&v2=&term=2-2024&a=s&cmd1=Search",
               "ESPA": "https://www.uprm.edu/registrar/sections/index.php?v1=ESPA&v2=&term=2-2024&a=s&cmd1=Search"}

# output for the export module
section_catalog = {}
course_catalog = {}

uprm_page = get(departments["CIIC"])

scrapped_page = parse_page(uprm_page.text, "html.parser")
catalog = scrapped_page.findAll("table", attrs={"class":"section_results"})

print(catalog[0]) # the course 

# print(uprm_page.text)

# we iterate only one time but we scrap the title alone and
# for k in departments:
#   uprm_page = get(departments[k])
#   #token_list = parser(uprm_page.text, "html.parser")
#   print()