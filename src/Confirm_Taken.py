from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import configparser
import mysql.connector

class ConfirmTaken(QWidget):
    selection_complete = pyqtSignal()  # Signal emitted when the course selection is complete
    switch_to_signup = pyqtSignal()

    def __init__(self, student_id, curriculum_id, current_semester):
        super().__init__()
        # Save the passed values for use in the class
        self.student_id = student_id
        self.curriculum_id = curriculum_id
        self.current_semester = current_semester

        # Database connection setup
        config = configparser.ConfigParser()
        config.read('credentials/db_config.ini')
        self.conn = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )
        self.cursor = self.conn.cursor()

        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Create the green banner
        banner = QLabel("Welcome to RegiUPR")
        banner.setStyleSheet("background-color: #4CAF50; color: black; font-size: 48px; font-weight: bold; padding: 20px;")
        banner.setAlignment(Qt.AlignCenter)
        banner.setFixedHeight(120)  # Increased height for more vertical space
        main_layout.addWidget(banner)

        # Create a spacer to push the input and button section to the center
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addItem(spacer)

        # Create a frame for the input fields and buttons
        central_frame = QWidget()
        central_layout = QHBoxLayout()  # Change to horizontal box layout
        central_frame.setLayout(central_layout)

        # Labels
        taken_label = QLabel("Select Courses You Have Already Taken and Are Currently Taking:")
        taken_label.setStyleSheet("font-weight: bold;")

        currently_taking_label = QLabel("Select Courses You Are Currently Taking:")
        currently_taking_label.setStyleSheet("font-weight: bold;")

        # Scroll areas for taken and currently taking courses
        taken_scroll = QScrollArea()
        taking_scroll = QScrollArea()
        taken_widget = QWidget()
        taking_widget = QWidget()
        taken_layout = QVBoxLayout()
        taking_layout = QVBoxLayout()

        # Populate checkboxes
        self.taken_checkboxes = []
        self.currently_taking_checkboxes = []
        self.populate_course_checkboxes(taken_layout, taking_layout)

        # Set up taken courses scroll area
        taken_widget.setLayout(taken_layout)
        taken_scroll.setWidget(taken_widget)
        taken_scroll.setWidgetResizable(True)

        # Set up currently taking courses scroll area
        taking_widget.setLayout(taking_layout)
        taking_scroll.setWidget(taking_widget)
        taking_scroll.setWidgetResizable(True)

        # Add labels and scroll areas to central layout
        taken_layout_with_label = QVBoxLayout()
        taken_layout_with_label.addWidget(taken_label)
        taken_layout_with_label.addWidget(taken_scroll)

        taking_layout_with_label = QVBoxLayout()
        taking_layout_with_label.addWidget(currently_taking_label)
        taking_layout_with_label.addWidget(taking_scroll)

        central_layout.addLayout(taken_layout_with_label)
        central_layout.addLayout(taking_layout_with_label)

        # Buttons
        button_layout = QHBoxLayout()

        confirm_button = QPushButton("Confirm Selection")
        confirm_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        confirm_button.setFixedWidth(200)  # Set fixed width to keep the buttons reasonable in size
        confirm_button.clicked.connect(self.confirm_selection)

        back_button = QPushButton("Back")
        back_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        back_button.setFixedWidth(200)  # Set fixed width to keep the buttons reasonable in size
        back_button.clicked.connect(self.go_back)

        # Add buttons side by side, without extra space
        button_layout.addStretch()
        button_layout.addWidget(confirm_button)
        button_layout.addWidget(back_button)
        button_layout.addStretch()

        # Add widgets to layout
        main_layout.addWidget(central_frame, alignment=Qt.AlignCenter)
        main_layout.addLayout(button_layout)

        # Add a spacer to push the content upwards
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(main_layout)
        self.setWindowTitle("Confirm Taken and Currently Taking Courses")
        self.setGeometry(100, 100, 800, 600)

    def populate_course_checkboxes(self, taken_layout, taking_layout):
        # Query to get all courses in the student's curriculum
        query = """
            SELECT cc.course_code, c.course_name, cc.semester
            FROM curriculum_courses cc
            JOIN courses c ON cc.course_code = c.course_code
            WHERE cc.curriculum_id = %s
        """
        try:
            self.cursor.execute(query, (self.curriculum_id,))
            results = self.cursor.fetchall()

            # Populate checkboxes based on the results
            for course_code, course_name, semester in results:
                # Checkbox for taken courses
                taken_checkbox = QCheckBox(f"{course_code} - {course_name} (Semester {semester})")
                taken_checkbox.setObjectName(course_code)
                taken_checkbox.setChecked(semester <= self.current_semester)  # Check if the semester is less than or equal to the current semester
                self.taken_checkboxes.append(taken_checkbox)
                taken_layout.addWidget(taken_checkbox)

                # Only add courses that are taken to the currently taking list
                if semester <= self.current_semester:
                    taking_checkbox = QCheckBox(f"{course_code} - {course_name} (Semester {semester})")
                    taking_checkbox.setObjectName(course_code)
                    taking_checkbox.setEnabled(True)  # Enable for courses taken
                    self.currently_taking_checkboxes.append(taking_checkbox)
                    taking_layout.addWidget(taking_checkbox)

                # Connect signals to enable/disable the currently taking checkbox
                taken_checkbox.stateChanged.connect(self.update_currently_taking_list)

        except mysql.connector.Error as err:
            # Handle database errors
            print(f"Database Error: {str(err)}")

    def update_currently_taking_list(self):
        """Update the currently taking courses list based on changes in the taken courses list."""
        for taken_checkbox, taking_checkbox in zip(self.taken_checkboxes, self.currently_taking_checkboxes):
            # Enable the corresponding "currently taking" checkbox if the taken checkbox is checked
            if taken_checkbox.isChecked():
                taking_checkbox.setEnabled(True)
            else:
                taking_checkbox.setEnabled(False)
                taking_checkbox.setChecked(False)

    def confirm_selection(self):
        try:
            # Update student_courses table based on selections
            for checkbox in self.taken_checkboxes:
                course_code = checkbox.objectName()
                if checkbox.isChecked():
                    # Query to get the relevant section_id for the course
                    section_query = """
                        SELECT section_id
                        FROM sections
                        WHERE course_code = %s
                        LIMIT 1
                    """
                    self.cursor.execute(section_query, (course_code,))
                    section_result = self.cursor.fetchone()

                    if section_result:
                        section_id = section_result[0]  # Get the section_id from the result
                        # Insert or update the student_courses table
                        query = """
                            INSERT INTO student_courses (student_id, course_code, section_id, status)
                            VALUES (%s, %s, %s, 'TAKEN')
                            ON DUPLICATE KEY UPDATE status = 'TAKEN'
                        """
                        self.cursor.execute(query, (self.student_id, course_code, section_id))

            for checkbox in self.currently_taking_checkboxes:
                course_code = checkbox.objectName()
                if checkbox.isChecked():
                    # Query to get the relevant section_id for the course
                    section_query = """
                        SELECT section_id
                        FROM sections
                        WHERE course_code = %s
                        LIMIT 1
                    """
                    self.cursor.execute(section_query, (course_code,))
                    section_result = self.cursor.fetchone()

                    if section_result:
                        section_id = section_result[0]  # Get the section_id from the result
                        # Insert or update the student_courses table
                        query = """
                            INSERT INTO student_courses (student_id, course_code, section_id, status)
                            VALUES (%s, %s, %s, 'Currently Taking')
                            ON DUPLICATE KEY UPDATE status = 'Currently Taking'
                        """
                        self.cursor.execute(query, (self.student_id, course_code, section_id))

            # Commit the changes to the database
            self.conn.commit()

            QMessageBox.information(self, "Account Created!", "Your Account Has Been Created! You Can Now Log In.")
            self.selection_complete.emit()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {str(err)}")
            self.conn.rollback()  # Rollback if there's an error

    def go_back(self):
        # Delete the temporary student data if going back
        try:
            cursor = self.conn.cursor()
            
            # Delete the student data from the database
            cursor.execute('''
                DELETE FROM students WHERE student_id = %s
            ''', (self.student_id,))

            self.conn.commit()  # Commit changes to delete the student data
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {str(err)}")
            self.conn.rollback()  # Rollback if there's an error
        # Emit signal to switch back to signup
        self.switch_to_signup.emit()

    def closeEvent(self, event):
        # Close the database connection when the widget is closed
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
        event.accept()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ConfirmTaken("802-12-3456", 1, 5)  # Example parameters for testing
    window.show()
    sys.exit(app.exec_())
