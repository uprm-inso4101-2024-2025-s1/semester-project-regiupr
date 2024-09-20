import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, 
                             QTableWidgetItem, QPushButton, QHBoxLayout, QMessageBox)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
from Main_Menu_Backend import MainMenuBackend  # Import the backend class

class MainMenu(QWidget):
    view_profile = pyqtSignal()  # Signal emitted to view profile
    logout = pyqtSignal()        # Signal emitted to log out
    view_courses = pyqtSignal()  # Signal emitted to view Course Enrollment

    student_info = {
        "student_id":"",
        "name":"",
        "email":"",
        "birthdate": "",
        "snn":"",
        "password":"",
    }

    def __init__(self, student_id):
        super().__init__()
        self.student_id = student_id  # Store the student ID
        self.main_menu_backend = MainMenuBackend(student_id)  # Pass student_id to backend

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
            left_panel_layout.setContentsMargins(10, 10, 10, 10)  # Adjust margins
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

        name = self.main_menu_backend.fetch_student_info()["name"]

        self.welcome_label = QLabel(f"Welcome, {name}!")  # Update to show student name
        self.welcome_label.setFont(QFont('Playfair Display', 24))
        center_layout.addWidget(self.welcome_label, alignment=Qt.AlignTop)
        
        schedule_label = QLabel("Enrollment Schedule")
        schedule_label.setFont(QFont('Playfair Display', 16))
        center_layout.addWidget(schedule_label)
        
        # Schedule Table
        self.schedule_table = QTableWidget(8, 7)  # 8 rows, 7 columns (days of the week)
        self.schedule_table.setHorizontalHeaderLabels(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        self.schedule_table.setVerticalHeaderLabels(["6:30 AM", "7:30 AM", "8:30 AM", "9:30 AM", "10:30 AM", "11:30 AM", "12:30 PM", "1:30 PM"])
        
        #self.populate_schedule()  # Populate schedule data
        
        center_layout.addWidget(self.schedule_table)
        
        # Bottom Table (Courses In Enrollment)
        courses_label = QLabel("Courses In Enrollment")
        courses_label.setFont(QFont('Playfair Display', 16))
        center_layout.addWidget(courses_label)
        
        self.enrollment_table = QTableWidget(5, 5)  # 5 columns for course details
        self.enrollment_table.setHorizontalHeaderLabels(["Curso", "Sección", "Créditos", "Reuniones", "Profesores"])
        
        self.populate_enrollment_courses()  # Populate enrollment data
        
        center_layout.addWidget(self.enrollment_table)
        center_panel.setLayout(center_layout)
        
        # Add panels to main layout
        main_layout.addWidget(left_panel)
        main_layout.addWidget(center_panel)
        
        self.setLayout(main_layout)
        self.setWindowTitle("RegiUPR")
        self.setGeometry(100, 100, 1200, 800)

    def populate_schedule(self):
        # Fetch and populate the student schedule
        schedule_courses = self.main_menu_backend.fetch_student_schedule()
        # Logic to populate the schedule table with schedule_courses data
        for row, course in enumerate(schedule_courses):
            # Assuming course contains data in the format suitable for display
            for column, day in enumerate(course['days']):
                self.schedule_table.setItem(row, column, QTableWidgetItem(day))

    def populate_enrollment_courses(self):
        # Fetch and populate the enrolled courses
        enrollment_data = self.main_menu_backend.fetch_enrolled_courses()
        for row, (course, section, credits, time, prof) in enumerate(enrollment_data):
            self.enrollment_table.setItem(row, 0, QTableWidgetItem(course))
            self.enrollment_table.setItem(row, 1, QTableWidgetItem(section))
            self.enrollment_table.setItem(row, 2, QTableWidgetItem(credits))
            self.enrollment_table.setItem(row, 3, QTableWidgetItem(time))
            self.enrollment_table.setItem(row, 4, QTableWidgetItem(prof))
        
        self.enrollment_table.setEditTriggers(QTableWidget.NoEditTriggers)

    def update_student_info(self, student_id):
        self.student_info = MainMenuBackend.fetch_student_info(student_id)
        

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
    student_id = 'your_student_id_here' 
    window = MainMenu(student_id)
    window.show()
    sys.exit(app.exec_())
