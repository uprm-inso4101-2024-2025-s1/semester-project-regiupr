import mysql.connector
import unittest
import sections

class TestSections(unittest.TestCase):

        def test_create(self):
                sections.create_section(conn, '080', 'INSO4101', 'Marko Schutz', 'MWF', '2:30p-3:20p', 'S113', 'Presential', '100')
                section=('080', 'INSO4101', 'Marko Schutz', 'MWF', '2:30p-3:20p', 'S113', 'Presential', 100)
                self.assertEqual(sections.select_section(conn,'080'), 
                                section,
                                'Create was unsuccessful')
                print('Current Sections:')
                sections.read_sections(conn)
                print('/////////////////////')
        
        def test_delete(self):
                sections.delete_section(conn, '080')
                self.assertEqual(sections.select_section(conn,'080'), 
                                None,
                                'Deletion was unsuccesful')
                print('Current Sections:')
                sections.read_sections(conn)
                print('/////////////////////')

        def test_select(self):
                sections.create_section(conn, '080', 'INSO4101', 'Marko Schutz', 'MWF', '2:30p-3:20p', 'S113', 'Presential', '100')
                self.assertEqual(sections.select_section(conn,'080'), 
                                        ('080', 'INSO4101', 'Marko Schutz', 'MWF', '2:30p-3:20p', 'S113', 'Presential', 100),
                                        'Selection was unsuccessful')
                print('Current Sections:')
                sections.read_sections(conn)
                print('/////////////////////')

        def test_update_prof(self):
                
                sections.update_section(conn, '080', professor_name='Fulano' )
                self.assertEqual(sections.select_section(conn,'080')[2], 
                                'Fulano',
                                'Update was unsuccessful')
                print('Current Sections:')
                sections.read_sections(conn)
                print('/////////////////////')
                
        def test_update_days(self):
                sections.update_section(conn, '080', days='TR' )
                self.assertEqual(sections.select_section(conn,'080')[3], 
                                'TR',
                                'Update was unsuccessful')
                print('Current Sections:')
                sections.read_sections(conn)
                print('/////////////////////')
                
        def test_update_schedule(self):
                sections.update_section(conn, '080', schedule='4:00-5:20' )
                self.assertEqual(sections.select_section(conn,'080')[4], 
                                '4:00-5:20',
                                'Update was unsuccessful')
                print('Current Sections:')
                sections.read_sections(conn)
                print('/////////////////////')
                
        def test_update_room(self):
                sections.update_section(conn, '080', room='S114' )
                self.assertEqual(sections.select_section(conn,'080')[5], 
                                'S114',
                                'Update was unsuccessful')
                print('Current Sections:')
                sections.read_sections(conn)
                print('/////////////////////')
                
        def test_update_modality(self):
                sections.update_section(conn, '080', modality='Online' )
                self.assertEqual(sections.select_section(conn,'080')[6], 
                                'Online' ,
                                'Update was unsuccessful')
                print('Current Sections:')
                sections.read_sections(conn)
                print('/////////////////////')
        
        def test_update_capacity(self):
                sections.update_section(conn, '080', capacity=200 )
                self.assertEqual(sections.select_section(conn,'080')[7], 
                                200,
                                'Update was unsuccessful')
                print('Current Sections:')
                sections.read_sections(conn)
                print('/////////////////////')
                
                


if __name__ == "__main__":
    conn = sections.create_connection()
    if conn:
        sections.delete_section(conn,'080')
        unittest.main()
        sections.delete_section(conn,'080')
        

conn.close()

