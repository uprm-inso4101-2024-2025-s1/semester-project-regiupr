import mysql.connector

import Sections
# Main execution
if __name__ == "__main__":
    conn = Sections.create_connection()
    if conn:
        # Example usage
        Sections.create_section(conn, '080', 'INSO4101', 'Marko Schutz', 'MWF', '2:00p-3:20p', 'S113', 'Presential', '100')
        Sections.read_sections(conn)
        Sections.update_section(conn, '080', schedule='2:30p-3:50p')
        Sections.select_sections(conn,'080')
        print("Section id:" + Sections._section_id_) 
        print("Course id:" + Sections._course_id_)
        print("Professor Name:" + Sections._professor_name_)
        print("Days:" + Sections._days_)
        print("Schedule:" + Sections._schedule_)
        print("Room:" + Sections._room_)
        print("Modality:" + Sections._modality_)
        print("Capacity:" + Sections._capacity_)
        Sections.delete_section(conn, '080')
        Sections.read_sections(conn)
        # Close the connection
        conn.close()
