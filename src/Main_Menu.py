import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, 
                             QTableWidgetItem, QPushButton, QHBoxLayout, QGridLayout, QDialog, QMessageBox)
from PyQt5.QtGui import QFont, QColor, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal

from gui_backend import Login_backend
from gui_backend import Profile_Backend
import mysql
import mysql.connector
import configparser
import Course_Enrollment
import random

class MainMenu(QWidget):
    view_profile = pyqtSignal()  # Signal emitted to view profile
    logout = pyqtSignal()        # Signal emitted to log out
    view_courses = pyqtSignal()  # Signal emitted to view Course Enrollment

    def __init__(self):
        super().__init__()
        # IMPORTANT
        # This was worked by the developer in charge of the main menu as a class. This HAVE TO BE refactored as
        # as module with only functions (such as the profile backend module) to avoid having to call unnecessarily
        # multiple modules
        #
        self.initUI()
        
    def initUI(self):
        # Main Layout
        main_layout = QHBoxLayout()
        
        # Left panel (green)
        left_panel = QWidget()
        left_panel_layout = QVBoxLayout()
        left_panel.setStyleSheet("background-color: #4CAF50;")
        
        # Adding Logo as an Image
        logo_label = QLabel(self)
        pixmap = QPixmap("src/resources/RegiUPR.png")  
        scaled_pixmap = pixmap.scaled(150, 100, Qt.KeepAspectRatio)  
        logo_label.setPixmap(scaled_pixmap)
        left_panel_layout.addWidget(logo_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        
        # Adding Buttons to the Left Panel
        self.btn_main_menu = QPushButton("Main Menu")
        self.btn_course_enroll = QPushButton("Course Enrollment")
        self.btn_profile = QPushButton("Profile")
        self.btn_logout = QPushButton("Logout")

        # Setting Button Styles
        button_style = """
            QPushButton {
                background-color: #D3D3D3;  
                color: black;
                font-size: 16px;
                font-family: 'Playfair Display', serif;
                padding: 10px;
                border: 2px solid black;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #B0B0B0;  
            }
        """
        
        for btn in [self.btn_main_menu, self.btn_course_enroll, self.btn_profile, self.btn_logout]:
            btn.setFixedSize(170, 50)  # Adjust button size (wider)
            btn.setStyleSheet(button_style)
            left_panel_layout.addWidget(btn, alignment=Qt.AlignTop)
            left_panel_layout.setContentsMargins(10, 10, 10, 10)  # Adjust margins (left, top, right, bottom)
            left_panel_layout.setSpacing(2)  # Reduce vertical spacing between buttons
            
        left_panel.setLayout(left_panel_layout)
        left_panel.setFixedWidth(200)

        # Connect button clicks to their respective slots
        self.btn_profile.clicked.connect(self.handle_profile)
        self.btn_logout.clicked.connect(self.confirm_logout)
        self.btn_course_enroll.clicked.connect(self.handle_courses)
        
        # Center panel (Content)
        center_panel = QWidget()
        center_layout = QVBoxLayout()
        
        # Problems with accessing directly to the main_menu_backend method, so the get_student_id function from
        # Login Backed inside has sustituted the main menu backend corresponing function 
        self.welcome_label = QLabel(f"Welcome, {Login_backend.get_student_info()[1]}!")  # Update to show student ID
        self.welcome_label.setFont(QFont('Playfair Display', 24))
        center_layout.addWidget(self.welcome_label, alignment=Qt.AlignTop)
        
        schedule_label = QLabel("Enrollment Schedule")
        schedule_label.setFont(QFont('Playfair Display', 16))
        center_layout.addWidget(schedule_label)
        
        # Schedule Table (Mockup with QTableWidget)
        schedule_table = QTableWidget(25, 7)  # 8 rows, 7 columns (days of the week)
        schedule_table.setHorizontalHeaderLabels(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        schedule_table.setVerticalHeaderLabels(["6:00 AM", "6:30 AM", "7:00 AM", "7:30 AM", "8:00 AM", "8:30 AM", "9:00 AM", "9:30 AM", 
                                                "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM", "12:00 PM", "12:30 PM", "1:00 PM","1:30 PM",
                                                "2:00 PM", "2:30 PM", "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM", "6:00 PM"])
        
        # # Adding colored blocks (mock schedule)
        # self.add_schedule_item(schedule_table, "MATE4009-030\nSalon: M-315", 3, 1, QColor(153, 204, 255), {
        #     "course": "MATE4009",
        #     "section": "030",
        #     "time": "9:30 AM - 10:20 AM",
        #     "professor": "Karen Rios Soto",
        #     "classroom": "M-315"
        # })  # Blue block
        
        # self.add_schedule_item(schedule_table, "ICOM4009-080\nSalon: S-113", 6, 4, QColor(204, 153, 255), {
        #     "course": "ICOM4009",
        #     "section": "080",
        #     "time": "2:30 PM - 3:20 PM",
        #     "professor": "Marko Schutz",
        #     "classroom": "S-113"
        # })  # Purple block

        #print("SECTIONS:", Course_Enrollment.ge)
        
        schedule_table.setEditTriggers(QTableWidget.NoEditTriggers)

        center_layout.addWidget(schedule_table)
        self.add_courses_to_schedule(schedule_table)
        
        # Bottom Table (Courses In Enrollment)
        courses_label = QLabel("Courses Currently Taking")
        courses_label.setFont(QFont('Playfair Display', 16))
        center_layout.addWidget(courses_label)
        
        enrollment_data = self.fetch_currently_taking_courses()
        print(enrollment_data)
        enrollment_table = QTableWidget(len(enrollment_data), 8)  # 5 columns for course details
        enrollment_table.setHorizontalHeaderLabels(["Curso", "Nombre", " Creditos", "Sección", "Profesor/a", "Reuniones", "Salón", "Modalidad"])
        
        for row, course_data in enumerate(enrollment_data):
            # Make sure the data is being accessed correctly
            course_code = course_data['course_code']
            course_name = course_data['course_name']
            credits = course_data['credits']
            section_id = course_data['section_id']
            professor_name = course_data['professor_name']
            schedule = course_data['schedule']
            room = course_data['room']
            modality = course_data['modality']
            # Populate the table row with the corresponding values
            enrollment_table.setItem(row, 0, QTableWidgetItem(course_code))
            enrollment_table.setItem(row, 1, QTableWidgetItem(course_name))
            enrollment_table.setItem(row, 2, QTableWidgetItem(str(credits)))
            enrollment_table.setItem(row, 3, QTableWidgetItem(section_id))
            enrollment_table.setItem(row, 4, QTableWidgetItem(professor_name))
            enrollment_table.setItem(row, 5, QTableWidgetItem(schedule))
            enrollment_table.setItem(row, 6, QTableWidgetItem(room))
            enrollment_table.setItem(row, 7, QTableWidgetItem(modality))
            
        enrollment_table.setEditTriggers(QTableWidget.NoEditTriggers)
        center_layout.addWidget(enrollment_table)
        center_panel.setLayout(center_layout)
        
        # Add panels to main layout
        main_layout.addWidget(left_panel)
        main_layout.addWidget(center_panel)
        
        self.setLayout(main_layout)
        self.setWindowTitle("RegiUPR")
        self.setGeometry(100, 100, 1200, 800)

    def add_courses_to_schedule(self, table):
        enrollment_data = self.fetch_currently_taking_courses()
        color_map = {}  # Map to store consistent colors for each course code

        for course_data in enrollment_data:
            course_code = course_data['course_code']
            course_name = course_data['course_name']
            schedule = course_data['schedule']
            section_id = course_data['section_id']
            professor_name = course_data['professor_name']
            room = course_data['room']
            modality = course_data['modality']

            # Prepare class details
            class_info = {
                "course_code": course_code,
                "course_name": course_name,
                "credits": course_data['credits'],
                "section_id": section_id,
                "professor_name": professor_name,
                "schedule": schedule,
                "room": room,
                "modality": modality,
            }

            # Assign a consistent color to the course
            if course_code not in color_map:
                # Generate pastel colors by ensuring high RGB values
                base = 200  # Minimum value to ensure pastel tones
                color_map[course_code] = QColor(
                    random.randint(base, 255),  # Red
                    random.randint(base, 255),  # Green
                    random.randint(base, 255),  # Blue
                )
            course_color = color_map[course_code]

            if modality != "Online":
                # Split the schedule into days and times
                days, time_range = schedule.split(" ")
                start_time, end_time = time_range.split("-")
                day_mapping = {"L": 1, "M": 2, "W": 3, "J": 4, "V": 5}  # Columns for each day

                try:
                    # Get the start and end rows for the time range
                    start_row = self.get_time_row(start_time)
                    end_row = self.get_time_row(end_time)
                except ValueError as e:
                    print(f"Error processing time range {time_range}: {e}")
                    continue

                # Add the course block for each day and time slot
                for day in days:
                    if day in day_mapping:
                        column = day_mapping[day]

                        # Ensure each block is only added once for the given day
                        for row in range(start_row, start_row+1):
                            if not table.item(row, column):  # Check if the cell is empty
                                self.add_schedule_item(
                                    table,
                                    f"{course_code}",
                                    row,
                                    column,
                                    course_color,
                                    class_info
                                )
            else:
                # For online courses, handle as needed
                print(f"Online course: {class_info}")


    def get_time_row(self, time):
        """Calculate the row index for a given time, based on 30-minute increments starting at 6:00 AM."""
        hours, minutes = map(int, time[:-2].split(':'))  # Extract hours and minutes
        period = time[-2:]  # AM/PM

        # Convert 12-hour format to 24-hour format
        if period == "PM" and hours != 12:
            hours += 12
        elif period == "AM" and hours == 12:
            hours = 0  # Handle midnight

        # Calculate minutes from 6:00 AM
        total_minutes_from_6am = (hours * 60 + minutes) - (6 * 60)

        # Ensure non-negative values (e.g., for times before 6:00 AM)
        if total_minutes_from_6am < 0:
            raise ValueError(f"Time {time} is before the schedule start of 6:00 AM.")

        # Convert to row index (30 minutes per row)
        row = total_minutes_from_6am // 30

        return row

    def add_schedule_item(self, table, text, row, column, color, class_info):
        """Add a schedule block to the table with proper formatting."""
        item = QTableWidgetItem(text)
        item.setBackground(color)
        table.setItem(row, column, item)

        # Make the item clickable to show course details
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item.setData(Qt.UserRole, class_info)
        table.cellClicked.connect(lambda r, c, row=row, column=column, class_info=class_info: self.show_class_info(r, c, row, column, class_info))

    def fetch_currently_taking_courses(self):
        try:
            config = configparser.ConfigParser()
            config.read('credentials/db_config.ini')
            db_connection = mysql.connector.connect(
                host=config['mysql']['host'],
                user=config['mysql']['user'],
                password=config['mysql']['password'],
                database=config['mysql']['database']
            )
            self.db_cursor = db_connection.cursor()
            self.student_data = Profile_Backend.get_student_data(Login_backend.get_student_info())
            # Define the SQL query to update the student's enrolled courses
            # This assumes that you have a column in the students table that stores enrolled courses
            # Modify the table and column names as needed
            self.student_id = self.student_data["student_id"]  # Function to get the currently logged-in student's ID
            query = """
            SELECT 
                sc.course_code, 
                c.course_name, 
                c.credits, 
                sc.section_id, 
                s.professor_name, 
                s.schedule, 
                s.room, 
                s.modality
            FROM 
                student_courses sc
            JOIN 
                sections s 
            ON 
                sc.section_id = s.section_id
            JOIN 
                courses c 
            ON 
                sc.course_code = c.course_code
            WHERE 
                sc.student_id = %s AND sc.status = 'Currently Taking';
            """
            self.db_cursor.execute(query, (self.student_id,))
            results = self.db_cursor.fetchall()
            courses = []
            for row in results:
                course = {
                    "course_code": row[0],
                    "course_name": row[1],
                    "credits": row[2],
                    "section_id": row[3],
                    "professor_name": row[4],
                    "schedule": row[5],
                    "room": row[6],
                    "modality": row[7]
                }
                courses.append(course)

            return courses

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def add_schedule_item(self, table, text, row, column, color, class_info):
        item = QTableWidgetItem(text)
        item.setBackground(color)
        table.setItem(row, column, item)
        
        # Connect the cell click event to show class info with the correct parameters
        table.cellClicked.connect(lambda r, c, class_info=class_info: self.show_class_info(r, c, row, column, class_info))

    def show_class_info(self, row, column, expected_row, expected_col, class_info):
        """Display detailed course information when a schedule block is clicked."""
        if row == expected_row and column == expected_col:
            dialog = QDialog(self)
            dialog.setWindowTitle("Class Information")
            layout = QVBoxLayout()
            
            # Populate the dialog with class info
            for key, value in class_info.items():
                layout.addWidget(QLabel(f"{key.replace('_', ' ').capitalize()}: {value}"))
            
            dialog.setLayout(layout)
            dialog.exec_()

    def handle_main_menu(self):
        pass  # Already on the Main Menu screen

    def handle_profile(self):
        self.view_profile.emit()

    def handle_courses(self):
        self.view_courses.emit()

    def confirm_logout(self):
        reply = QMessageBox.question(self, 'Log Out',
                                     "Are you sure you want to log out?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.logout.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())