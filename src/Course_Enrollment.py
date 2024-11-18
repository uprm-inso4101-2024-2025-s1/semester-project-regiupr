import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QLineEdit, QWidget, QFrame, QScrollArea, QGridLayout, QMessageBox)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
import configparser
import mysql.connector
from gui_backend import Profile_Backend
from gui_backend import Login_backend

def generate_class_days():
    day_map = {
        "Monday, Wednesday, Friday": "MWF",
        "Monday, Wednesday": "MW",
        "Tuesday, Thursday": "TT",
        "Monday, Tuesday, Wednesday, Thursday": "MTWT",
        "Friday": "F"
    }
    return day_map[random.choice(list(day_map.keys()))]

def generate_class_hours():
    start_hour = random.randint(8, 19)  # 8am to 8pm
    start_minute = random.choice([0, 30])
    end_hour = start_hour
    end_minute = start_minute + 50
    if end_minute >= 60:
        end_minute -= 60
        end_hour += 1
    if end_hour > 19:
        end_hour = 19
        end_minute = 0

    start_period = "AM" if start_hour < 12 else "PM"
    end_period = "AM" if end_hour < 12 else "PM"
    start_hour = start_hour if start_hour <= 12 else start_hour - 12
    end_hour = end_hour if end_hour <= 12 else end_hour - 12
    end_hour = 12 if end_hour == 0 else end_hour

    return f"{start_hour}:{start_minute:02d}{start_period} - {end_hour}:{end_minute:02d}{end_period}"

def generate_sections():
    sections = []
    for _ in range(random.randint(3, 5)):
        section_code = f"0{random.randint(10, 99)}"
        class_days = generate_class_days()
        class_hours = generate_class_hours()
        available = random.choice([True, False])
        sections.append({
            "section_code": section_code,
            "days": class_days,
            "hours": class_hours,
            "available": available
        })
    return sections

class CourseEnroll(QWidget):
    view_profile = pyqtSignal()
    logout = pyqtSignal()
    view_main_menu = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("RegiUPR © Software")
        self.setGeometry(100, 100, 1200, 800)

        self.main_layout = QHBoxLayout(self)
        self.create_side_panel()
        self.content_layout = QVBoxLayout()
        self.create_banner()
        self.create_search_area()
        self.create_result_area()

        content_container = QWidget()
        content_container.setLayout(self.content_layout)
        self.main_layout.addWidget(content_container)
        self.setLayout(self.main_layout)

        self.enrolled_classes = []
        self.courses = self.load_courses_from_database()

    def create_side_panel(self):
        left_panel = QWidget()
        left_panel_layout = QVBoxLayout()
        left_panel.setStyleSheet("background-color: #4CAF50;")

        logo_label = QLabel(self)
        pixmap = QPixmap("src/resources/RegiUPR.png")  
        scaled_pixmap = pixmap.scaled(150, 100, Qt.KeepAspectRatio)  
        logo_label.setPixmap(scaled_pixmap)
        left_panel_layout.addWidget(logo_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        button_style = """
            QPushButton {
                background-color: #D3D3D3;  
                color: black;
                font-size: 16px;
                padding: 10px;
                border: 2px solid black;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #B0B0B0;  
            }
        """

        self.btn_main_menu = QPushButton("Main Menu")
        self.btn_course_enrollment = QPushButton("Course Enrollment")
        self.btn_profile = QPushButton("Profile")
        self.btn_logout = QPushButton("Logout")

        for btn in [self.btn_main_menu, self.btn_course_enrollment, self.btn_profile, self.btn_logout]:
            btn.setFixedSize(170, 50)
            btn.setStyleSheet(button_style)
            left_panel_layout.addWidget(btn, alignment=Qt.AlignTop)

        left_panel.setLayout(left_panel_layout)
        left_panel.setFixedWidth(200)

        self.btn_profile.clicked.connect(self.handle_profile)
        self.btn_logout.clicked.connect(self.confirm_logout)
        self.btn_main_menu.clicked.connect(self.handle_main_menu)

        self.main_layout.addWidget(left_panel)

    def create_banner(self):
        banner_frame = QFrame(self)
        banner_frame.setStyleSheet("background-color: #4CAF50; height: 100px;")
        banner_layout = QHBoxLayout(banner_frame)

        title_label = QLabel("RegiUPR Course Enrollment System ™")
        title_label.setStyleSheet("color: white;")
        title_label.setFont(QFont("Playfair Display", 16, QFont.Bold))
        banner_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        self.content_layout.addWidget(banner_frame)

    def create_search_area(self):
        search_layout = QVBoxLayout()

        title_label = QLabel("Insert Course Code Below. Ex: ICOM4009")
        title_label.setFont(QFont("Playfair Display", 12))
        search_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        self.search_bar = QLineEdit()
        self.search_bar.setFont(QFont("Playfair Display", 14))
        self.search_bar.setPlaceholderText("Enter course code...")
        self.search_bar.textChanged.connect(self.on_search)
        search_layout.addWidget(self.search_bar, alignment=Qt.AlignCenter)

        self.error_label = QLabel()
        self.error_label.setFont(QFont("Playfair Display", 12, QFont.Bold))
        self.error_label.setStyleSheet("color: red;")
        search_layout.addWidget(self.error_label, alignment=Qt.AlignCenter)

        self.content_layout.addLayout(search_layout)

    def create_result_area(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_area.setWidget(self.scroll_content)
        self.result_layout = QGridLayout(self.scroll_content)

        self.content_layout.addWidget(self.scroll_area)

    def load_courses_from_database(self):
        config = configparser.ConfigParser()
        config.read('credentials/db_config.ini')
        self.db_connection = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )
        self.db_cursor = self.db_connection.cursor(dictionary=True)
        self.db_cursor.execute("SELECT * FROM courses")
        courses = self.db_cursor.fetchall()
        course_list = []
        for row in courses:
            course_info = {
                "course_code": row["course_code"],
                "course_name": row["course_name"],
                "description": row["description"],
                "credits": row["credits"],
                "program": row["program"],
                "sections": generate_sections()
            }
            course_list.append(course_info)
        self.db_cursor.close()
        self.db_connection.close()
        return course_list

    def on_search(self, text):
        query = text.strip().lower()
        if query:
            results = self.search_courses(query)
            if results:
                self.error_label.setText("")
                self.display_results(results)
            else:
                self.error_label.setText("No courses found. Please make sure you are entering a valid course code.")
                self.clear_results()
        else:
            self.clear_results()

    def search_courses(self, query):
        return [
            course for course in self.courses
            if query in course['course_code'].lower() or query in course['course_name'].lower()
        ]

    def display_results(self, results):
        self.clear_results()
        row = 0
        for course in results:
            card_frame = QFrame(self)
            card_frame.setFrameShape(QFrame.Box)
            card_frame.setLineWidth(2)
            card_layout = QVBoxLayout()

            course_code_label = QLabel(f"<b>{course['course_code']} - {course['course_name']}</b>")
            card_layout.addWidget(course_code_label)

            sections_list = ', '.join([section['section_code'] for section in course['sections']])
            sections_label = QLabel(f"Sections: {sections_list}")
            card_layout.addWidget(sections_label)

            department_label = QLabel(f"<b>Department: {course['program']}</b>")
            card_layout.addWidget(department_label)

            button_layout = QHBoxLayout()
            details_button = QPushButton("More Details")
            details_button.setEnabled(False)
            enroll_button = QPushButton("Enroll")
            enroll_button.clicked.connect(lambda checked, c=course: self.show_sections(c))
            button_layout.addWidget(details_button)
            button_layout.addWidget(enroll_button)

            card_layout.addLayout(button_layout)
            card_frame.setLayout(card_layout)
            self.result_layout.addWidget(card_frame, row, 0)
            row += 1

    def show_sections(self, course):
        self.sections_window = QMainWindow(self)
        self.sections_window.setWindowTitle("Available Sections")
        self.sections_window.setGeometry(150, 150, 600, 400)

        sections_widget = QWidget()
        sections_layout = QVBoxLayout(sections_widget)

        for section in course['sections']:
            section_frame = QFrame(self)
            section_frame.setFrameShape(QFrame.Box)
            section_frame.setLineWidth(1)

            section_layout = QVBoxLayout()

            section_code_label = QLabel(f"<b>Section: {section['section_code']}</b>")
            section_layout.addWidget(section_code_label)

            section_days_label = QLabel(f"Days: {section['days']}")
            section_layout.addWidget(section_days_label)

            section_hours_label = QLabel(f"Hours: {section['hours']}")
            section_layout.addWidget(section_hours_label)

            if section["available"]:
                enroll_button = QPushButton("Enroll in Section")
                enroll_button.clicked.connect(lambda checked, s=section: self.enroll_in_section(course, s))
                section_layout.addWidget(enroll_button)
            else:
                not_available_label = QLabel("Section is Full")
                section_layout.addWidget(not_available_label)

            section_frame.setLayout(section_layout)
            sections_layout.addWidget(section_frame)

        self.sections_window.setCentralWidget(sections_widget)
        self.sections_window.show()

    def enroll_in_section(self, course, section):
        if section["available"]:
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
                INSERT INTO student_courses (student_id, course_code, section_id, status)
                VALUES (%s, %s, %s, 'Currently Taking')
                ON DUPLICATE KEY UPDATE status = 'Currently Taking'
                """
                self.db_cursor.execute(query, (
                    self.student_id,  # Replace with the logged-in student ID
                    course["course_code"],
                    section["section_code"]
                ))
                self.db_connection.commit()

                # Add course to the local list of enrolled classes
                self.enrolled_classes.append({
                    "course_code": course["course_code"],
                    "course_name": course["course_name"],
                    "section_code": section["section_code"],
                    "days": section["days"],
                    "hours": section["hours"]
                })

                QMessageBox.information(self, "Enrollment Success",
                                        f"You have successfully enrolled in {course['course_code']} - Section {section['section_code']}")
                if self.db_connection.is_connected():
                    self.db_cursor.close()
                    self.db_connection.close()
                self.sections_window.close()
            except Exception as e:
                QMessageBox.critical(self, "Database Error", f"An error occurred: {str(e)}")
        else:
            QMessageBox.warning(self, "Enrollment Failed", "This section is full. Please choose another section.")


    def clear_results(self):
        for i in reversed(range(self.result_layout.count())):
            widget_to_remove = self.result_layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)

    def handle_profile(self):
        self.view_profile.emit()

    def confirm_logout(self):
        response = QMessageBox.question(self, "Logout", "Are you sure you want to logout?", 
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if response == QMessageBox.Yes:
            self.logout.emit()

    def handle_main_menu(self):
        self.view_main_menu.emit()

    def closeEvent(self, event):
        if hasattr(self, 'db_connection') and self.db_connection.is_connected():
            self.db_cursor.close()
            self.db_connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CourseEnroll()
    window.show()
    sys.exit(app.exec_())
