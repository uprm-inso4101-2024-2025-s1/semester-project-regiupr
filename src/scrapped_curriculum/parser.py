# For scrapping the src html code of the web
from requests import get
# For parsing on the web
from bs4 import BeautifulSoup as parser
# 
import csv

# This should be moved in another file as a csv and then moved here, for organization purposes 
departments = {"CIIC": "https://www.uprm.edu/registrar/sections/index.php?v1=CIIC&v2=&term=2-2024&a=s&cmd1=Search",
               "ADMI": "https://www.uprm.edu/registrar/sections/index.php?v1=ADMI&v2=&term=2-2024&a=s&cmd1=Search",
               "ESPA": "https://www.uprm.edu/registrar/sections/index.php?v1=ESPA&v2=&term=2-2024&a=s&cmd1=Search"}

uprm_page = get(departments["CIIC"])
print(uprm_page.text)

# for k in departments:
#   uprm_page = get(departments[k])
#   #token_list = parser(uprm_page.text, "html.parser")
#   print()