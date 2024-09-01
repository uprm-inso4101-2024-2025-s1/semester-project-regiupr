import csv, os

# This goes to the resources folder and loads the file with the lexicon being used in the interface
csv_file_path = os.path.join(os.path.dirname(__file__), 'resources', 'language.csv')

# Dictionary with other dictionaries with the text groups corresponding to each language
languages = {} 

def load_languages_from_csv(filepath):
    # langauge of the section in the csv file being read
    current_language = ""

    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "LANG":
                languages[row[1]] = {}
                current_language = row[1]
            else:
                languages[current_language][row[0]] = row[1:]

def selected_language(lang_name):
    return languages[lang_name]