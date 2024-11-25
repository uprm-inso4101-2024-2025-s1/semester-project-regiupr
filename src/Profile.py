import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from datetime import datetime, timedelta
import configparser
import mysql.connector
from DB_connection import StudentsM

from gui_backend import Profile_Backend
from gui_backend import Login_Backend

class Profile(QWidget):
    view_main_menu = pyqtSignal()  # Signal emitted to view main menu
    logout = pyqtSignal()         # Signal emitted to log out
    view_courses = pyqtSignal()  # Signal emitted to view Course Enrollment
    view_college_planning = pyqtSignal() # Signal emitted to view College Planning

    student_data = {
        "student_id": "",
        "name": "",
        "email": "",
        "birthdate": "",
        "ssn": "",
        "password": "",
        "curriculum_id": "",
    }

    def __init__(self):
        super().__init__()

        self.reset_profile()
        self.setWindowTitle("Profile Page")
        self.setGeometry(100, 100, 900, 600)
        self.last_edit_date = None  # Track last edit date for 15-day restriction
        self.password_shown = False  # Track if the password is shown or hidden

        # Main layout
        main_layout = QHBoxLayout(self)

        # Left panel
        left_panel = QWidget()
        left_panel_layout = QVBoxLayout()
        left_panel.setStyleSheet("background-color: #4CAF50;")

        # Adding Logo
        logo_label = QLabel(self)
        pixmap = QPixmap("src/resources/RegiUPR.png")
        scaled_pixmap = pixmap.scaled(150, 100, Qt.KeepAspectRatio)
        logo_label.setPixmap(scaled_pixmap)
        left_panel_layout.addWidget(logo_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        # Adding Buttons to the Left Panel
        self.btn_main_menu = QPushButton("Main Menu")
        self.btn_course_enroll = QPushButton("Course Enrollment")
        self.btn_college_planning = QPushButton("College Planning")
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

        for btn in [self.btn_main_menu, self.btn_course_enroll, self.btn_college_planning, self.btn_profile, self.btn_logout]:
            btn.setFixedSize(170, 50)  # Adjust button size (wider)
            btn.setStyleSheet(button_style)
            left_panel_layout.addWidget(btn, alignment=Qt.AlignTop)
            left_panel_layout.setContentsMargins(10, 10, 10, 10)  # Adjust margins
            left_panel_layout.setSpacing(2)  # Reduce vertical spacing between buttons

        left_panel.setLayout(left_panel_layout)
        left_panel.setFixedWidth(200)

        # Connect button clicks to their respective slots
        self.btn_main_menu.clicked.connect(self.handle_main_menu)
        self.btn_course_enroll.clicked.connect(self.handle_courses)
        self.btn_college_planning.clicked.connect(self.handle_college_planning)
        self.btn_logout.clicked.connect(self.confirm_logout)

        # Add left panel to main layout
        main_layout.addWidget(left_panel)

        # Profile form
        self.profile_form = self.create_profile_form()
        self.form_widget = QWidget()
        self.form_widget.setLayout(self.profile_form)

        # Center the form in a layout
        form_layout = QVBoxLayout()
        form_layout.addStretch(1)
        form_layout.addWidget(self.form_widget, alignment=Qt.AlignCenter)
        form_layout.addStretch(1)
        main_layout.addLayout(form_layout)

    def create_profile_form(self):
        # Create form layout
        form_layout = QFormLayout()

        # Increase the size of the input fields
        input_style = """
            QLineEdit {
                font-size: 18px;
                padding: 10px;
                font-family: 'Playfair Display', serif;
            }
        """

        # Style for labels (bigger and bold)
        label_style = """
                QLabel {
                font-size: 20px;
                font-weight: bold;
                font-family: 'Playfair Display', serif;
                }
        """

        # Message label
        self.message_label = QLabel("User can only change the password and email information.")
        self.message_label.setStyleSheet("font-size: 16px; font-weight: bold; color: black;")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.hide()  # Initially hidden
        
        # Add Profile Picture
        profile_pic_label = QLabel(self)
        try:
            profile_pixmap = QPixmap("src/resources/ProfileIcon.png")
            if profile_pixmap.isNull():
                raise FileNotFoundError("Profile image not found.")
            scaled_pixmap = profile_pixmap.scaled(200, 200, Qt.KeepAspectRatio)
            profile_pic_label.setPixmap(scaled_pixmap)
        except FileNotFoundError:
            profile_pic_label.setText("Profile Image Missing")
            profile_pic_label.setStyleSheet("font-size: 18px; color: red;")
        
        profile_pic_label.setAlignment(Qt.AlignCenter)  # Center the profile picture
        form_layout.addWidget(profile_pic_label)

        # Add Name (Non-editable)
        name_label = QLabel("Name")
        name_label.setStyleSheet(label_style)  # Apply label style
        name_field = QLineEdit(self.student_data["name"])
        name_field.setReadOnly(True)
        name_field.setStyleSheet(input_style)

        # Add Student ID (Non-editable)
        id_label = QLabel("Student ID")
        id_label.setStyleSheet(label_style)  # Apply label style
        id_field = QLineEdit(self.student_data["student_id"])
        id_field.setReadOnly(True)
        id_field.setStyleSheet(input_style)

        # Add Password (Initially non-editable)
        self.password_label = QLabel("Password")
        self.password_label.setStyleSheet(label_style)  # Apply label style
        self.password_field = QLineEdit(str(self.student_data["password"]))
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setReadOnly(True)
        self.password_field.setStyleSheet(input_style)

        # Add "Show" clickable text
        self.show_hide_label = QLabel("<a href='#'>show</a>")
        self.show_hide_label.setStyleSheet("font-size: 14px; font-family: 'Playfair Display', serif; color: blue;")
        self.show_hide_label.setOpenExternalLinks(False)
        self.show_hide_label.linkActivated.connect(self.toggle_password_visibility)

        # Add Email (Initially non-editable)
        self.email_label = QLabel("Email")
        self.email_label.setStyleSheet(label_style)  # Apply label style
        self.email_field = QLineEdit(self.student_data["email"])
        self.email_field.setReadOnly(True)
        self.email_field.setStyleSheet(input_style)

        # Add Degree (Non-editable)
        degree_label = QLabel("Degree")
        degree_label.setStyleSheet(label_style)  # Apply label style
        degree_field = QLineEdit(self.get_program_name())
        degree_field.setReadOnly(True)
        degree_field.setStyleSheet(input_style)

        # Add Enrollment Status (Non-editable)
        status_label = QLabel("Enrollment Status")
        status_label.setStyleSheet(label_style)  # Apply label style
        status_field = QLineEdit(self.get_enrollment_status())
        status_field.setReadOnly(True)
        status_field.setStyleSheet(input_style)

        # Add Edit Info button
        self.edit_button = QPushButton("Edit Info")
        self.edit_button.setStyleSheet("background-color: green; color: white; font-size: 14px; padding: 10px;")
        self.edit_button.clicked.connect(self.enable_edit)

        # Add Delete Account button
        self.delete_button = QPushButton("Delete Account")
        self.delete_button.setStyleSheet("background-color: red; color: white; font-size: 14px; padding: 10px;")
        self.delete_button.clicked.connect(self.delete_account)

        # Add Save Changes button (Initially hidden)
        self.save_button = QPushButton("Save Changes")
        self.save_button.setStyleSheet("background-color: blue; color: white; font-size: 14px; padding: 10px;")
        self.save_button.hide()
        self.save_button.clicked.connect(self.save_changes)

        # Add Cancel button (Initially hidden)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("background-color: red; color: white; font-size: 14px; padding: 10px;")
        self.cancel_button.hide()
        self.cancel_button.clicked.connect(self.cancel_edit)

        # Add fields to the form
        form_layout.addRow(name_label, name_field)
        form_layout.addRow(id_label, id_field)

        # Add password with show/hide functionality
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_field)
        password_layout.addWidget(self.show_hide_label)
        form_layout.addRow(self.password_label, password_layout)

        form_layout.addRow(self.email_label, self.email_field)
        form_layout.addRow(degree_label, degree_field)
        form_layout.addRow(status_label, status_field)

        # Add message label to the top of the form
        form_layout.insertRow(0, self.message_label)  # Insert message label at the top of the form

        # Add buttons to the form
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.delete_button)
        form_layout.addRow(button_layout)
        form_layout.addRow(self.save_button, self.cancel_button)

        return form_layout

    def get_program_name(self):
        # Get program name based on curriculum_id
        config = configparser.ConfigParser()
        config.read('credentials/db_config.ini')
        conn = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )
        cursor = conn.cursor()
        cursor.execute("SELECT program FROM curriculum WHERE curriculum_id = %s", (self.student_data["curriculum_id"],))
        result = cursor.fetchone()
        print(result)
        conn.close()
        return result[0] if result else "N/A"

    def get_enrollment_status(self):
        # Determine enrollment status based on the student_courses table
        config = configparser.ConfigParser()
        config.read('credentials/db_config.ini')
        conn = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(*) 
            FROM student_courses 
            WHERE student_id = %s AND (status = 'Currently Taking' OR status = 'ENROLLED')
        """, (self.student_data["student_id"],))
        result = cursor.fetchone()
        conn.close()
        return "ENROLLED" if result[0] > 0 else "NOT ENROLLED"

    def delete_account(self):
        reply = QMessageBox.question(self, 'Delete Account',
                                     "Are you sure you want to delete your account? This action cannot be undone.",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                # Delete student from the database
                config = configparser.ConfigParser()
                config.read('credentials/db_config.ini')
                conn = mysql.connector.connect(
                    host=config['mysql']['host'],
                    user=config['mysql']['user'],
                    password=config['mysql']['password'],
                    database=config['mysql']['database']
                )
                cursor = conn.cursor()
                cursor.execute("DELETE FROM student_courses WHERE student_id = %s", (self.student_data["student_id"],))
                cursor.execute("DELETE FROM students WHERE student_id = %s", (self.student_data["student_id"],))
                conn.commit()
                conn.close()
                QMessageBox.information(self, "Account Deleted", "Account Successfully Deleted!")
                self.logout.emit()
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Database Error", f"An error occurred: {str(err)}")

    #run this whenever you want to update data being displayed
    def reset_profile(self):
        self.student_data = Profile_Backend.get_student_data(Login_Backend.get_student_info())

    def toggle_password_visibility(self):
        # Toggle between showing and hiding the password
        if self.password_shown:
            self.password_field.setEchoMode(QLineEdit.Password)
            self.show_hide_label.setText("<a href='#'>show</a>")
            self.password_shown = False
        else:
            self.password_field.setEchoMode(QLineEdit.Normal)
            self.show_hide_label.setText("<a href='#'>hide</a>")
            self.password_shown = True

    def enable_edit(self):
        # Check if 15 days have passed since last edit
        if self.last_edit_date and (datetime.now() - self.last_edit_date).days < 15:
            QMessageBox.warning(self, "Edit Restricted", f"Cannot make edits until {self.last_edit_date + timedelta(days=15):%Y-%m-%d}")
            return
        # Get the original values from student_data
        self.current_password = self.student_data["password"]
        self.current_email = self.student_data["email"]
        # Enable editing of email and password
        self.password_field.setReadOnly(False)
        self.email_field.setReadOnly(False)
        self.edit_button.hide()  # Hide Edit button
        self.delete_button.hide()  # Hide Delete Account button
        self.save_button.show()  # Show Save button
        self.cancel_button.show()  # Show Cancel button

    def save_changes(self):
        new_password = self.password_field.text()
        new_email = self.email_field.text()
        if new_password == self.current_password and new_email == self.current_email:
            # Discard changes and reset the form
            self.password_field.setText(str(self.student_data["password"]))
            self.email_field.setText(self.student_data["email"])
            self.save_button.hide()
            self.cancel_button.hide()
            self.edit_button.show()
            self.delete_button.show()
        else:
            reply = QMessageBox.question(self, 'Confirm Changes',
                                        "Are you sure you want to keep these changes? (User won't be allowed to make changes for another 15 days)",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                config = configparser.ConfigParser()
                config.read('credentials/db_config.ini')
                conn = mysql.connector.connect(
                    host=config['mysql']['host'],
                    user=config['mysql']['user'],
                    password=config['mysql']['password'],
                    database=config['mysql']['database']
                )
                cursor = conn.cursor()
                if new_password != self.current_password:
                    cursor.execute("UPDATE students SET password = %s WHERE student_id = %s", (new_password, self.student_data["student_id"]))
                if new_email != self.current_email:
                    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, self.student_data["student_id"]))
                conn.commit()
                conn.close()
                self.password_field.setReadOnly(True)
                self.email_field.setReadOnly(True)
                self.last_edit_date = datetime.now()
                self.save_button.hide()
                self.cancel_button.hide()
                self.edit_button.show()
                self.delete_button.show()
            else:
                # Allow user to continue editing
                pass

    def cancel_edit(self):
        # Discard changes and reset the form
        self.password_field.setText(str(self.student_data["password"]))
        self.email_field.setText(self.student_data["email"])
        self.save_button.hide()
        self.cancel_button.hide()
        self.edit_button.show()
        self.delete_button.show()
        self.password_field.setReadOnly(True)
        self.email_field.setReadOnly(True)

    def handle_main_menu(self):
        self.view_main_menu.emit()

    def handle_courses(self):
        self.view_courses.emit()

    def handle_college_planning(self):
        self.view_college_planning.emit()

    def confirm_logout(self):
        reply = QMessageBox.question(self, 'Log Out',
                                     "Are you sure you want to log out?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.logout.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Profile()
    window.show()
    sys.exit(app.exec_())
