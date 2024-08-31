
# ---
# NOTE: 
# - The words and sentences should be stored apropietly in a csv 
# or txt file and not loaded in a list.
#
# - This module should be in another folder diferent from 'src', but 
# that will require further work with os.path
# ---

# ENGLIST
txt_en_other = ["Department", "More Details", "Enroll", "Details for", "Details for", "Select Section for", "<Configure>"]
txt_en_enroll_section = ["Enroll" ] # f"Do you want to enroll in Section {section['section_code']} for {course['code']}?"

txt_doc_EN = [txt_en_other, txt_en_enroll_section]

#SPANISH
txt_doc_ES = []


def selected_language(lang_id):
    match lang_id:
        case 1:
            return txt_doc_EN
        case 2:
            return txt_doc_ES