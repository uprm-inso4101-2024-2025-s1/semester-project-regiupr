
#
# NOTE: 
# - The words and sentences should be stored apropietly in a csv 
# or txt file and not loaded in a list.
#
# - This module should be in another folder diferent from 'src', but 
# that will require further work with os.path
#

txt_doc_EN = ["testing", "text"]
txt_doc_ES = ["probando", "texto"]

def selected_language(lang_id):
    match lang_id:
        case 1:
            return txt_doc_EN
        case 2:
            return txt_doc_ES