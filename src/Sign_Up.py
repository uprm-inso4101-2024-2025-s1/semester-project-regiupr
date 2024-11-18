import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import configparser
import mysql.connector
from sqlite3 import *
import re
from DB_connection import StudentsM 
from gui_backend.Login_Backend import verify_credentials
import hashlib

class SignUp(QWidget):
    
    logout = pyqtSignal()

    def __init__(self):
        super().__init__()

        config = configparser.ConfigParser()
        config.read('credentials/db_config.ini')
        self.conn = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )


        self.setWindowTitle("Create New Account")
        self.setGeometry(100, 100, 800, 600)  # Set a default size for the window
        self.setWindowState(Qt.WindowMaximized)  # Start maximized

        # Create the main layout
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
        central_layout = QVBoxLayout()
        central_frame.setLayout(central_layout)
        
        # Create a form layout for the input fields
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for more control over spacing
        form_layout.setHorizontalSpacing(20)  # Add spacing between labels and inputs
        form_layout.setVerticalSpacing(20)  # Add spacing between rows

        # Set the font for labels and entries
        label_font = QFont('Playfair Display', 14, QFont.Bold)
        entry_font = QFont('Playfair Display', 16)

        self.first_name_entry = QLineEdit()
        self.first_name_entry.setFont(entry_font)
        self.first_name_entry.textChanged.connect(self.verify_first_alpha)
        self.first_name_entry.returnPressed.connect(self.focus_next_last)

        self.last_name_entry = QLineEdit()
        self.last_name_entry.setFont(entry_font)
        self.last_name_entry.textChanged.connect(self.verify_last_alpha)
        self.last_name_entry.returnPressed.connect(self.focus_next_bday)

        self.birthdate_entry = QDateEdit(self)
        self.birthdate_entry.setCalendarPopup(True)
        self.birthdate_entry.setDisplayFormat("yyyy-MM-dd")  # Set display format
        # Set today's date as the default date in the QDateEdit widget
        self.birthdate_entry.setDate(QDate.currentDate())

        self.ssn_entry = QLineEdit()
        self.ssn_entry.setFont(entry_font)
        self.ssn_entry.textChanged.connect(self.format_ssn)
        self.ssn_entry.returnPressed.connect(self.focus_next_stuid)

        self.sid_entry = QLineEdit()
        self.sid_entry.setPlaceholderText("Ex: 802-12-3456")
        self.sid_entry.setFont(entry_font)
        self.sid_entry.textChanged.connect(self.format_student_id)
        self.sid_entry.returnPressed.connect(self.focus_next_email)

        self.email_entry = QLineEdit()
        self.email_entry.setPlaceholderText("Ex: student.name@upr.edu")
        self.email_entry.setFont(entry_font)
        self.email_entry.textChanged.connect(self.limit_email_input)
        self.email_entry.returnPressed.connect(self.focus_next_pass)

        self.new_pass = QLineEdit()
        self.new_pass.setPlaceholderText("Password Here")
        self.new_pass.setFont(entry_font)
        self.new_pass.setEchoMode(QLineEdit.Password)
        self.new_pass.returnPressed.connect(self.focus_next_confirm)
        
        self.confirm_pass = QLineEdit()
        self.confirm_pass.setPlaceholderText("Confirm Password")
        self.confirm_pass.setFont(entry_font)
        self.confirm_pass.setEchoMode(QLineEdit.Password)
        self.confirm_pass.returnPressed.connect(self.confirm_creation)

        # Create a toggle for showing/hiding password as clickable text
        self.toggle_button = QPushButton("Show")
        self.toggle_button.setFont(QFont('Playfair Display', 13))
        self.toggle_button.setStyleSheet("border: none; color: black; text-decoration: underline;")
        self.toggle_button.clicked.connect(self.toggle_password_visibility)
        
        # Add Student ID (Non-editable)
        first_label = QLabel("First Name")
        first_label.setFont(label_font)

        last_label = QLabel("Last Name")
        last_label.setFont(label_font)

        bday_label = QLabel("Birth Date")
        bday_label.setFont(label_font)

        ssn_label = QLabel("SSN")
        ssn_label.setFont(label_font)

        id_label = QLabel("Student ID")
        id_label.setFont(label_font)

        email_label = QLabel("Email")
        email_label.setFont(label_font)

        password_label = QLabel("Password")
        password_label.setFont(label_font)

        confirm_label = QLabel("Confirm Password")
        confirm_label.setFont(label_font)

        # Add widgets to the form layout
        form_layout.addRow(first_label, self.first_name_entry)
        form_layout.addRow(last_label, self.last_name_entry)
        form_layout.addRow(bday_label, self.birthdate_entry)
        form_layout.addRow(ssn_label, self.ssn_entry)
        form_layout.addRow(id_label, self.sid_entry)
        form_layout.addRow(email_label, self.email_entry)

        # Create a layout for the password input and toggle button
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.new_pass)
        password_layout.addWidget(self.toggle_button)
        form_layout.addRow(password_label, password_layout)

        confirm_layout = QHBoxLayout()
        confirm_layout.addWidget(self.confirm_pass)
        confirm_layout.addWidget(self.toggle_button)
        form_layout.addRow(confirm_label, confirm_layout)
        
        central_layout.addLayout(form_layout)

        button_layout = QHBoxLayout()

        self.createButton = QPushButton("Create Account")
        self.createButton.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        self.createButton.clicked.connect(self.confirm_creation)
        self.backButton = QPushButton("Back")
        self.backButton.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        self.backButton.clicked.connect(self.go_back)

        button_layout.addWidget(self.createButton)
        button_layout.addWidget(self.backButton)

        central_layout.addLayout(button_layout)
        
        # Set maximum width for the input and button frame
        central_frame.setMaximumWidth(600)
        
        # Add the central frame to the main layout
        main_layout.addWidget(central_frame, alignment=Qt.AlignCenter)
        
        # Add a spacer to push the content upwards
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        self.setLayout(main_layout)

    def toggle_password_visibility(self):
        if self.confirm_pass.echoMode() == QLineEdit.Password:
            self.new_pass.setEchoMode(QLineEdit.Normal)
            self.confirm_pass.setEchoMode(QLineEdit.Normal)
            self.toggle_button.setText("Hide")
        else:
            self.new_pass.setEchoMode(QLineEdit.Password)
            self.confirm_pass.setEchoMode(QLineEdit.Password)
            self.toggle_button.setText("Show")

    def format_student_id(self, text):
        # Remove any non-digit and non-dash characters
        text = ''.join([char for char in text if char.isdigit() or char == '-'])
        
        # Remove dashes for formatting purposes
        digits = text.replace("-", "")
        
        # Format the string with dashes if enough digits are present
        if len(digits) > 3:
            digits = digits[:3] + '-' + digits[3:]
        if len(digits) > 6:
            digits = digits[:6] + '-' + digits[6:]
        
        # Limit to 9 digits (excluding dashes)
        if len(digits.replace('-', '')) > 9:
            digits = digits[:11]  # 9 digits + 2 dashes
        
        # Set the formatted text back to the input field
        self.sid_entry.setText(digits)

    def format_ssn(self, text):
        # Remove any non-digit and non-dash characters
        text = ''.join([char for char in text if char.isdigit() or char == '-'])
        
        # Remove dashes for formatting purposes
        digits = text.replace("-", "")
        
        # Format the string with dashes if enough digits are present
        if len(digits) > 3:
            digits = digits[:3] + '-' + digits[3:]
        if len(digits) > 6:
            digits = digits[:6] + '-' + digits[6:]
        
        # Limit to 9 digits (excluding dashes)
        if len(digits.replace('-', '')) > 9:
            digits = digits[:11]  # 9 digits + 2 dashes
        
        # Set the formatted text back to the input field
        self.ssn_entry.setText(digits)

    def limit_email_input(self):
        text = self.email_entry.text()

        # Regex pattern to match valid email format with a top-level domain (e.g., .com, .net, .edu)
        email_pattern = r"^[^@]+@[^@]+\.[a-zA-Z]{3,4}$"
        
        # Check if the input matches the email pattern
        if re.match(email_pattern, text):
            # If the email matches the pattern, truncate the input and prevent further typing
            self.email_entry.setMaxLength(len(text))
        else:
            # Allow further typing if the email format is not yet complete
            self.email_entry.setMaxLength(100)  # Set a reasonable max length for email input

       
    def verify_first_alpha(self):
        text = self.first_name_entry.text()  # Replace with the relevant QLineEdit input field

        # Allow only alphabetic characters (letters)
        cleaned_text = re.sub(r'[^a-zA-Z]', '', text)
        
        # Limit input to a specific number of characters (e.g., 20 characters)
        max_length = 20
        if len(cleaned_text) > max_length:
            cleaned_text = cleaned_text[:max_length]
        
        # Update the input field without affecting the cursor position
        self.first_name_entry.blockSignals(True)  # Prevent triggering textChanged again
        self.first_name_entry.setText(cleaned_text)
        self.first_name_entry.blockSignals(False)

    def verify_last_alpha(self):
        text = self.last_name_entry.text()  # Replace with the relevant QLineEdit input field

        # Allow only alphabetic characters (letters)
        cleaned_text = re.sub(r'[^a-zA-Z]', '', text)
        
        # Limit input to a specific number of characters (e.g., 20 characters)
        max_length = 20
        if len(cleaned_text) > max_length:
            cleaned_text = cleaned_text[:max_length]
        
        # Update the input field without affecting the cursor position
        self.last_name_entry.blockSignals(True)  # Prevent triggering textChanged again
        self.last_name_entry.setText(cleaned_text)
        self.last_name_entry.blockSignals(False)
    
    def focus_next_last(self):
        """Move focus to the Last Name input when Enter is pressed in the first name field."""
        if self.first_name_entry.hasAcceptableInput():  # Only move if the email is valid
            self.last_name_entry.setFocus()

    def focus_next_bday(self):
        """Move focus to the Birthdate input when Enter is pressed in the last name field."""
        if self.last_name_entry.hasAcceptableInput():
            self.birthdate_entry.setFocus()
    
    def focus_next_stuid(self):
        """Move focus to the Student ID input when Enter is pressed in the last name field."""
        if self.ssn_entry.hasAcceptableInput():  # Only move if the email is valid
            self.sid_entry.setFocus()

    def focus_next_email(self):
        """Move focus to the Email input when Enter is pressed in the student id field."""
        if self.sid_entry.hasAcceptableInput():  # Only move if the email is valid
            self.email_entry.setFocus()

    def focus_next_pass(self):
        """Move focus to the password input when Enter is pressed in the email field."""
        if self.email_entry.hasAcceptableInput():  # Only move if the email is valid
            self.new_pass.setFocus()
    
    def focus_next_confirm(self):
        """Move focus to the confirm password input when Enter is pressed in the password field."""
        if self.new_pass.hasAcceptableInput():  # Only move if the email is valid
            self.confirm_pass.setFocus()

    def go_back(self):
        self.first_name_entry.clear()
        self.last_name_entry.clear()
        self.birthdate_entry.clear()
        self.ssn_entry.clear()
        self.sid_entry.clear()
        self.email_entry.clear()
        self.new_pass.clear()
        self.confirm_pass.clear()
        self.logout.emit()

    def confirm_creation(self):
        self.name = self.first_name_entry.text() + " " + self.last_name_entry.text()
        self.student_id = self.sid_entry.text()
        self.email = self.email_entry.text()
        self.birthdate = self.birthdate_entry.text()
        ssn_text = self.ssn_entry.text().replace('-', '')
        self.ssn = int(ssn_text)
        self.password = self.confirm_pass.text()

        if (verify_credentials(self.email_entry.text(), self.sid_entry.text(), self.confirm_pass.text())):
            QMessageBox.warning(self, "Account Found", "Account Already Exists! Try Again")
        else:
            confirm = QMessageBox.question(self, 'Confirm Account Creation',
                                     "Confirm details are correct and create account?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if confirm == QMessageBox.Yes:
                cursor = self.conn.cursor()
                # Use a parameterized query and wrap column names in backticks (`) to avoid conflicts
                cursor.execute('''
                    INSERT INTO `students` (`student_id`, `name`, `email`, `birthdate`, `ssn`, `password`)
                    VALUES (%s, %s, %s, %s, %s, %s)
                ''', (self.student_id, self.name, self.email, self.birthdate, self.ssn, self.password))

                # Commit the transaction to save the changes permanently
                self.conn.commit()
                QMessageBox.information(self, "Account Created", "Account has been created! You may now log in to RegiUPR.")
                StudentsM.fetch_table(self.conn)
                self.logout.emit()
                self.conn.close()
            else:
            # Do nothing, allow user to continue editing
                pass
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = SignUp()
    window.show()
    sys.exit(app.exec_())

    