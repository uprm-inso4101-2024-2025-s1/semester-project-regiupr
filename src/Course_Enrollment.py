import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QLineEdit, QWidget, QFrame, QScrollArea, QGridLayout, QMessageBox)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
import configparser
import mysql.connector
from gui_backend import Profile_Backend
from gui_backend import Login_Backend

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
        self.student_data = Profile_Backend.get_student_data(Login_Backend.get_student_info())
        self.student_id = self.student_data["student_id"]  # Function to get the currently logged-in student's ID

        # Fetch all courses
        self.db_cursor.execute("SELECT * FROM courses")
        courses = self.db_cursor.fetchall()

        course_list = []
        for row in courses:
            course_code = row['course_code']

            # Check student's status for the course
            self.db_cursor.execute("""
                SELECT status 
                FROM student_courses 
                WHERE student_id = %s AND course_code = %s
            """, (self.student_id, course_code))
            status = self.db_cursor.fetchone()

            # Skip courses with "TAKEN" status
            if status and status["status"] == "TAKEN":
                continue

            # Fetch sections for the course
            self.db_cursor.execute("""
                SELECT section_id 
                FROM sections 
                WHERE course_code = %s
            """, (course_code,))
            sections = [section["section_id"] for section in self.db_cursor.fetchall()]

            # Determine if the course can be enrolled
            if status and status["status"] == "CURRENTLY TAKING":
                enrollable = False
                status_message = "Course Is Currently Being Taken"
            else:
                enrollable = True
                status_message = None

            # Add course info to the list
            course_info = {
                "course_code": row["course_code"],
                "course_name": row["course_name"],
                "description": row["description"],
                "credits": row["credits"],
                "program": row["program"],
                "sections": sections,
                "enrollable": enrollable,
                "status_message": status_message
            }
            course_list.append(course_info)

        # Close the database connection
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
        filtered_courses = []
        for course in self.courses:
            # Skip courses with status "TAKEN"
            if course.get('status') == "TAKEN":
                continue

            # Match query with course code or name
            if query in course['course_code'].lower() or query in course['course_name'].lower():
                filtered_courses.append(course)

        return filtered_courses
    
    def display_results(self, results):
        self.clear_results()
        row = 0
        for course in results:
            card_frame = QFrame(self)
            card_frame.setFrameShape(QFrame.Box)
            card_frame.setLineWidth(2)
            card_layout = QVBoxLayout()

            # Course Code and Name
            course_code_label = QLabel(f"<b>{course['course_code']} - {course['course_name']}</b>")
            card_layout.addWidget(course_code_label)

            # Sections
            sections_list = ', '.join(course['sections'])
            sections_label = QLabel(f"Sections: {sections_list}")
            card_layout.addWidget(sections_label)

            # Department
            department_label = QLabel(f"<b>Department: {course['program']}</b>")
            card_layout.addWidget(department_label)

            # Status Message
            if course.get('status_message'):
                status_label = QLabel(f"<i>{course['status_message']}</i>")
                status_label.setStyleSheet("color: red;")
                card_layout.addWidget(status_label)

            # Buttons
            button_layout = QHBoxLayout()
            details_button = QPushButton("More Details")
            enroll_button = QPushButton("Enroll")

            # Disable buttons if not enrollable
            if not course.get('enrollable', True):
                details_button.setEnabled(False)
                enroll_button.setEnabled(False)

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

        # Database connection to fetch section details with capacities
        config = configparser.ConfigParser()
        config.read('credentials/db_config.ini')
        db_connection = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )
        db_cursor = db_connection.cursor(dictionary=True)

        # Fetch sections for the course
        db_cursor.execute("SELECT * FROM sections WHERE course_code = %s", (course['course_code'],))
        sections = db_cursor.fetchall()

        if not sections:
            sections_label = QLabel("No sections available for this course.")
            sections_layout.addWidget(sections_label)
        else:
            for section in sections:
                section_frame = QFrame(self)
                section_frame.setFrameShape(QFrame.Box)
                section_frame.setLineWidth(1)

                section_layout = QVBoxLayout()

                section_code_label = QLabel(f"<b>Section: {section['section_id']}</b>")
                section_layout.addWidget(section_code_label)

                section_sched_label = QLabel(f"Schedule: {section['schedule']}")
                section_layout.addWidget(section_sched_label)

                section_prof_label = QLabel(f"Professor: {section['professor_name']}")
                section_layout.addWidget(section_prof_label)

                capacity = section['capacity']
                if capacity > 0:
                    enroll_button = QPushButton("Enroll in Section")
                    enroll_button.clicked.connect(lambda checked, s=section: self.enroll_in_section(course, s))
                    section_layout.addWidget(enroll_button)
                else:
                    not_available_label = QLabel(f"Capacity is full. Can't enroll in this section for {course['course_name']}")
                    section_layout.addWidget(not_available_label)

                section_frame.setLayout(section_layout)
                sections_layout.addWidget(section_frame)

        db_cursor.close()
        db_connection.close()

        self.sections_window.setCentralWidget(sections_widget)
        self.sections_window.show()

    def enroll_in_section(self, course, section):
        try:
            # Prompt to confirm enrollment
            confirm = QMessageBox.question(
                self,
                "Confirm Enrollment",
                f"Confirm enrollment for section {section['section_id']} of course {course['course_code']}?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            # If the user confirms the enrollment
            if confirm == QMessageBox.Yes:
                # Database connection setup
                config = configparser.ConfigParser()
                config.read('credentials/db_config.ini')
                db_connection = mysql.connector.connect(
                    host=config['mysql']['host'],
                    user=config['mysql']['user'],
                    password=config['mysql']['password'],
                    database=config['mysql']['database']
                )
                db_cursor = db_connection.cursor()

                # Get the student ID
                self.student_data = Profile_Backend.get_student_data(Login_Backend.get_student_info())
                student_id = self.student_data["student_id"]

                # Check if capacity is greater than 0
                if section['capacity'] > 0:
                    # Update the student_courses table
                    query = """
                        INSERT INTO student_courses (student_id, course_code, section_id, status)
                        VALUES (%s, %s, %s, 'Enrolled For Next Semester')
                    """
                    db_cursor.execute(query, (student_id, course['course_code'], section['section_id']))

                    # Decrease the capacity of the section
                    update_capacity_query = "UPDATE sections SET capacity = capacity - 1 WHERE section_id = %s"
                    db_cursor.execute(update_capacity_query, (section['section_id'],))

                    # Commit the changes to the database
                    db_connection.commit()

                    QMessageBox.information(self, "Enrollment Success",
                                            f"You have successfully enrolled in {course['course_name']} - Section {section['section_id']}")

                    # Close the sections window after enrollment
                    self.sections_window.close()

                else:
                    QMessageBox.warning(self, "Enrollment Failed",
                                        f"Capacity is full. Can't enroll in this section for {course['course_name']}")

                # Close the database connection
                if db_connection.is_connected():
                    db_cursor.close()
                    db_connection.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {str(err)}")


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