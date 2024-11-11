import csv
from collections import defaultdict

# It should make sure that the getter of this return it when it has already populated by the parser
UI_content_strings = {}

# The parser should be run only one in a app execution, so unnecesary delays are avoided.
def parse_UI_content_string_document(file_path):
    # Dictionary to store organized content
    content_dict = defaultdict(lambda: defaultdict(list))
    current_language = None

    # Open and read the CSV file
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        for row in reader:
            # Skip empty rows or rows with fewer than 2 columns
            if len(row) < 2:
                continue
            
            # Detect language change with "LANG" keyword
            if row[0].strip() == "LANG":
                current_language = row[1].strip().lower()
            elif current_language:  # If language is set, add row content
                module = row[0].strip()
                # Add modile content to the current language
                content_dict[current_language][module].extend(row[1:])

    return content_dict

# Path to the CSV file
#file_path = 'resources/language_texts.csv'

parse_UI_content_string_document()

def get_text():
    return UI_content_strings

# At the end of the parsing, UI_content_strings should have the following structure:
#
# UI_content_strings_test = {
#     "english":{"module_1":["text", "word"], "module_2":["text", "word"]},
#     "spanish":{"module_1":["texto", "palabra"], "module_2":["texto", "pakabra"]},
#     "keys":{
#         "another key":["values"], 
#         "another key 2":["values"]
#     }
# }
#
# And if it's not enough clear:
#
# B_1 = {"module name":"and its UI content strings"}
# B_2 = {"module name":"你好, the text (which is this value) should change according the language, but the keys MUST remain the same"}
# A = {"lang B1":B_1, "lang B2":B_2}
#
# Basically, A is a dictionary that has B dictionaries inside, each of which has the name of the module 
# or section as keys and the text strings as values. These B dictionaries are also values ​​of dictionary A, 
# which has as keys the name of the language in which the text strings of the values ​​of dictionaries B are.