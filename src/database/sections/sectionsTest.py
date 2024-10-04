import mysql.connector

import sections
# Main execution
if __name__ == "__main__":
    conn = sections.create_connection()
    if conn:
        # Example usage
        sections.create_section(conn, '080', 'INSO4101', 'Marko Schutz', 'MWF', '2:00p-3:20p', 'S113', 'Presential', '100')
        sections.read_sections(conn)
        sections.update_section(conn, '080', schedule='2:30p-3:50p')
        sections.select_sections(conn,'080')
        print("Section id:" + sections._section_id_) 
        print("Course id:" + sections._course_id_)
        print("Professor Name:" + sections._professor_name_)
        print("Days:" + sections._days_)
        print("Schedule:" + sections._schedule_)
        print("Room:" + sections._room_)
        print("Modality:" + sections._modality_)
        print("Capacity:" + sections._capacity_)
        sections.delete_section(conn, '080')
        sections.read_sections(conn)
        # Close the connection
        conn.close()