import sys
import csv
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QLineEdit, QWidget, QFrame, QScrollArea, QGridLayout, QMessageBox)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal

def generate_class_days():
    day_map = {
        "Monday, Wednesday, Friday": "LWV",
        "Monday, Wednesday": "LW",
        "Tuesday, Thursday": "MJ",
        "Monday, Tuesday, Wednesday, Thursday": "LMWJ",
        "Friday": "V"
    }
    days = list(day_map.keys())
    return day_map[random.choice(days)]

def generate_class_hours():
    start_hour = random.randint(8, 19)  # 8am to 8pm
    start_minute = random.choice([0, 30])
    end_hour = start_hour
    end_minute = start_minute + 50
    if end_minute >= 60:
        end_minute -= 60
        end_hour += 1
    if end_hour > 19:  # Ensure it does not go past 8pm
        end_hour = 19
        end_minute = 0

    # Convert to 12-hour format
    start_period = "AM" if start_hour < 12 else "PM"
    end_period = "AM" if end_hour < 12 else "PM"
    start_hour = start_hour if start_hour <= 12 else start_hour - 12
    end_hour = end_hour if end_hour <= 12 else end_hour - 12

    # If end hour is zero, set it to 12 (for cases like 00:30)
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
    view_profile = pyqtSignal()  # Signal emitted to view profile
    logout = pyqtSignal()        # Signal emitted to log out
    view_main_menu = pyqtSignal()  # Signal emitted to view main menu

    def __init__(self):
        super().__init__()

        self.setWindowTitle("RegiUPR © Software")
        self.setGeometry(100, 100, 1200, 800)

        # Main Layout
        self.main_layout = QHBoxLayout(self)

        # Add the green side panel (fixed)
        self.create_side_panel()

        # Add the main content area
        self.content_layout = QVBoxLayout()
        self.create_banner()
        self.create_search_area()
        self.create_result_area()

        # Create a container widget for the main content area
        content_container = QWidget()
        content_container.setLayout(self.content_layout)

        # Add the content container to the main layout (next to the side panel)
        self.main_layout.addWidget(content_container)

        # Set the layout of the main window
        self.setLayout(self.main_layout)

        self.enrolled_classes = []
        self.courses = self.load_courses_from_csv('src/resources/CatalogoCursos.csv')  # Load courses from CSV file

    def create_side_panel(self):
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
        self.btn_main_menu.clicked.connect(self.handle_main_menu)

        # Add the left panel to the main layout
        self.main_layout.addWidget(left_panel)

    def create_banner(self):
        banner_frame = QFrame(self)
        banner_frame.setStyleSheet("background-color: #4CAF50; height: 100px;")
        banner_layout = QHBoxLayout(banner_frame)

        # Add title
        title_label = QLabel("RegiUPR Course Enrollment System ™")
        title_label.setStyleSheet("color: white;")
        title_label.setFont(QFont("Playfair Display", 16, QFont.Bold))
        banner_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        self.content_layout.addWidget(banner_frame)

    def create_search_area(self):
        search_layout = QVBoxLayout()

        # Title label
        title_label = QLabel("Insert Course Code Below. Ex: ICOM4009")
        title_label.setFont(QFont("Playfair Display", 12))
        search_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Search bar
        self.search_bar = QLineEdit()
        self.search_bar.setFont(QFont("Playfair Display", 14))
        self.search_bar.setPlaceholderText("Enter course code...")
        self.search_bar.textChanged.connect(self.on_search)
        search_layout.addWidget(self.search_bar, alignment=Qt.AlignCenter)

        # Error label
        self.error_label = QLabel()
        self.error_label.setFont(QFont("Playfair Display", 12, QFont.Bold))
        self.error_label.setStyleSheet("color: red;")
        search_layout.addWidget(self.error_label, alignment=Qt.AlignCenter)

        self.content_layout.addLayout(search_layout)

    def create_result_area(self):
        # Scroll area for search results
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_area.setWidget(self.scroll_content)
        self.result_layout = QGridLayout(self.scroll_content)

        self.content_layout.addWidget(self.scroll_area)

    def load_courses_from_csv(self, filepath):
        courses = []
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                course = {
                    "department": row['department'],
                    "code": row['code'],
                    "name": row['name'],
                    "sections": generate_sections()
                }
                courses.append(course)
        return courses

    def on_search(self, text):
        query = text.strip().lower()
        if query:
            results = self.search_courses(query)
            if results:
                self.error_label.setText("")
                self.display_results(results)
            else:
                self.error_label.setText("No courses found. Please make sure you are entering a valid course code.")
                self.clear_results()  # Ensure results are cleared if no valid courses are found
        else:
            self.clear_results()  # Clear results when the search input is empty

    def search_courses(self, query):
        return [course for course in self.courses if query in course['code'].lower()]

    def display_results(self, results):
        self.clear_results()
        row = 0
        for course in results:
            card_frame = QFrame(self)
            card_frame.setFrameShape(QFrame.Box)
            card_frame.setLineWidth(2)
            card_layout = QVBoxLayout()

            # Course Code and Name
            course_code_label = QLabel(f"<b>{course['code']} - {course['name']}</b>")
            card_layout.addWidget(course_code_label)

            # Sections
            sections_list = ', '.join([section['section_code'] for section in course['sections']])
            sections_label = QLabel(f"Sections: {sections_list}")
            card_layout.addWidget(sections_label)


            # Department
            department_label = QLabel(f"<b>Department: {course['department']}</b>")
            card_layout.addWidget(department_label)

            # Buttons
            button_layout = QHBoxLayout()
            details_button = QPushButton("More Details")
            details_button.setEnabled(False)  # Disabled as per requirement
            enroll_button = QPushButton("Enroll")
            enroll_button.clicked.connect(lambda checked, c=course: self.show_sections(c))
            button_layout.addWidget(details_button)
            button_layout.addWidget(enroll_button)

            card_layout.addLayout(button_layout)

            card_frame.setLayout(card_layout)
            self.result_layout.addWidget(card_frame, row, 0)
            row += 1

    def show_sections(self, course):
        self.sections_window = QMainWindow(self)  # Store the sections window as an instance variable
        self.sections_window.setWindowTitle("Available Sections")
        self.sections_window.setGeometry(150, 150, 600, 400)

        sections_widget = QWidget()
        sections_layout = QVBoxLayout(sections_widget)

        for section in course['sections']:
            section_frame = QFrame(self)
            section_frame.setFrameShape(QFrame.Box)
            section_frame.setLineWidth(2)
            section_layout = QVBoxLayout()

            # Section Details
            section_label = QLabel(f"<b>Section: {section['section_code']}</b>")
            days_label = QLabel(f"Days: {section['days']}")
            hours_label = QLabel(f"Class Time: {section['hours']}")
            availability_label = QLabel(f"<b>Availability: {'Yes' if section['available'] else 'No'}</b>")
            section_layout.addWidget(section_label)
            section_layout.addWidget(days_label)
            section_layout.addWidget(hours_label)
            section_layout.addWidget(availability_label)

            # Enroll Button
            enroll_button = QPushButton("Enroll")
            enroll_button.setEnabled(section['available'])
            enroll_button.clicked.connect(lambda _, s=section: self.confirm_enroll(s, course['code']))
            section_layout.addWidget(enroll_button)

            section_frame.setLayout(section_layout)
            sections_layout.addWidget(section_frame)

        self.sections_window.setCentralWidget(sections_widget)
        self.sections_window.show()

    def confirm_enroll(self, section, course_code):
        reply = QMessageBox.question(self, "Confirm Enrollment", 
                                    f"Are you sure you want to enroll in Section {section['section_code']} of {course_code}?", 
                                    QMessageBox.Yes | QMessageBox.No, 
                                    QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.enrolled_classes.append(section)
            QMessageBox.information(self, "Enrolled", f"Enrolled in Section {section['section_code']} of {course_code}.")
            self.sections_window.close()

    def clear_results(self):
        for i in reversed(range(self.result_layout.count())):
            widget = self.result_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def handle_enroll(self, section):
        if section['available']:
            confirm = QMessageBox.question(self, "Enroll", f"Do you want to enroll in Section {section['section_code']}?", QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.enrolled_classes.append(section)
                QMessageBox.information(self, "Enrolled", "You have been successfully enrolled in the section.")
        else:
            QMessageBox.warning(self, "Enrollment Failed", "This section is not available.")

    def handle_profile(self):
        self.view_profile.emit()

    def handle_main_menu(self):
        self.view_main_menu.emit()

    def confirm_logout(self):
        confirm = QMessageBox.question(self, "Logout", "Are you sure you want to logout?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.logout.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CourseEnroll()
    window.show()
    sys.exit(app.exec_())