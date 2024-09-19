import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, 
                             QTableWidgetItem, QPushButton, QHBoxLayout, QGridLayout, QDialog, QMessageBox)
from PyQt5.QtGui import QFont, QColor, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal

class MainMenu(QWidget):
    view_profile = pyqtSignal()  # Signal emitted to view profile
    logout = pyqtSignal()        # Signal emitted to log out
    view_courses = pyqtSignal()  # Signal emitted to view Course Enrollment

    def __init__(self):
        super().__init__()
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
        
        welcome_label = QLabel("Welcome, User!")
        welcome_label.setFont(QFont('Playfair Display', 24))
        center_layout.addWidget(welcome_label, alignment=Qt.AlignTop)
        
        schedule_label = QLabel("Enrollment Schedule")
        schedule_label.setFont(QFont('Playfair Display', 16))
        center_layout.addWidget(schedule_label)
        
        # Schedule Table (Mockup with QTableWidget)
        schedule_table = QTableWidget(8, 7)  # 8 rows, 7 columns (days of the week)
        schedule_table.setHorizontalHeaderLabels(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        schedule_table.setVerticalHeaderLabels(["6:30 AM", "7:30 AM", "8:30 AM", "9:30 AM", "10:30 AM", "11:30 AM", "12:30 PM", "1:30 PM"])
        
        # Adding colored blocks (mock schedule)
        self.add_schedule_item(schedule_table, "MATE4009-030\nSalon: M-315", 3, 1, QColor(153, 204, 255), {
            "course": "MATE4009",
            "section": "030",
            "time": "9:30 AM - 10:20 AM",
            "professor": "Karen Rios Soto",
            "classroom": "M-315"
        })  # Blue block
        
        self.add_schedule_item(schedule_table, "ICOM4009-080\nSalon: S-113", 6, 4, QColor(204, 153, 255), {
            "course": "ICOM4009",
            "section": "080",
            "time": "2:30 PM - 3:20 PM",
            "professor": "Marko Schutz",
            "classroom": "S-113"
        })  # Purple block
        
        schedule_table.setEditTriggers(QTableWidget.NoEditTriggers)

        center_layout.addWidget(schedule_table)
        
        # Bottom Table (Courses In Enrollment)
        courses_label = QLabel("Courses In Enrollment")
        courses_label.setFont(QFont('Playfair Display', 16))
        center_layout.addWidget(courses_label)
        
        enrollment_table = QTableWidget(5, 5)  # 5 columns for course details
        enrollment_table.setHorizontalHeaderLabels(["Curso", "Sección", "Créditos", "Reuniones", "Profesores"])
        enrollment_data = [
            ("INEL3105", "040", "3", "10:30 am - 11:20 am", "Jose M Rosado Roman"),
            ("INEL4205", "036", "3", "9:00 am - 10:15 am", "Hamed Parsiani Gobadi"),
            ("MATE4009", "030", "3", "9:30 am - 10:20 am", "Karen Rios Soto"),
            ("INGE3045", "086", "3", "2:00 pm - 3:15 pm", "Agnes Padovani Blanco"),
            ("ICOM4009", "080", "3", "2:30 pm - 3:20 pm", "Marko Schutz")
        ]
        
        for row, (course, section, credits, time, prof) in enumerate(enrollment_data):
            enrollment_table.setItem(row, 0, QTableWidgetItem(course))
            enrollment_table.setItem(row, 1, QTableWidgetItem(section))
            enrollment_table.setItem(row, 2, QTableWidgetItem(credits))
            enrollment_table.setItem(row, 3, QTableWidgetItem(time))
            enrollment_table.setItem(row, 4, QTableWidgetItem(prof))
        
        enrollment_table.setEditTriggers(QTableWidget.NoEditTriggers)
        center_layout.addWidget(enrollment_table)
        center_panel.setLayout(center_layout)
        
        # Add panels to main layout
        main_layout.addWidget(left_panel)
        main_layout.addWidget(center_panel)
        
        self.setLayout(main_layout)
        self.setWindowTitle("RegiUPR")
        self.setGeometry(100, 100, 1200, 800)

    def add_schedule_item(self, table, text, row, column, color, class_info):
        item = QTableWidgetItem(text)
        item.setBackground(color)
        table.setItem(row, column, item)
        
        # Connect the cell click event to show class info with the correct parameters
        table.cellClicked.connect(lambda r, c, class_info=class_info: self.show_class_info(r, c, row, column, class_info))

    def show_class_info(self, row, column, expected_row, expected_col, class_info):
        # Check if the clicked cell is the expected class block cell
        if row == expected_row and column == expected_col:
            dialog = QDialog(self)
            dialog.setWindowTitle("Class Information")
            
            # Dialog layout
            layout = QVBoxLayout()
            course_label = QLabel(f"Course: {class_info['course']}")
            section_label = QLabel(f"Section: {class_info['section']}")
            time_label = QLabel(f"Time: {class_info['time']}")
            professor_label = QLabel(f"Professor: {class_info['professor']}")
            classroom_label = QLabel(f"Classroom: {class_info['classroom']}")
            
            layout.addWidget(course_label)
            layout.addWidget(section_label)
            layout.addWidget(time_label)
            layout.addWidget(professor_label)
            layout.addWidget(classroom_label)
            
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