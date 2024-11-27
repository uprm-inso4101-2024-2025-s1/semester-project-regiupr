from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSignal
from Forgot_EmailVal import ForgotEmailVal
from gui_backend.Login_backend import start_login, verify_credentials
import re

#language
from Language import UI_content_strings, current_language
text = UI_content_strings[current_language]

class Login(QWidget):
    login_successful = pyqtSignal()  # Signal emitted on successful login
    switch_to_forgot_password = pyqtSignal()
    switch_to_signup = pyqtSignal()

    def __init__(self):
        super().__init__()
        
        print(current_language, "test")

        start_login()
        self.setWindowTitle("Login to RegiUPR")
        self.setGeometry(100, 100, 800, 600)  # Set a default size for the window
        self.setWindowState(Qt.WindowMaximized)  # Start maximized
        
        # Create the main layout
        main_layout = QVBoxLayout()
        
        # Create the green banner
        banner = QLabel(text["_general_prelogin"][0]) # LANG TEST
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
        
        # Create input widgets with placeholder text
        self.user_entry = QLineEdit()
        self.user_entry.setPlaceholderText(text["Login"][3]) # "Ex: student.name@upr.edu"
        self.user_entry.setFont(entry_font)
        self.user_entry.textChanged.connect(self.limit_email_input)
        self.user_entry.returnPressed.connect(self.focus_next_sid)
        
        self.sid_entry = QLineEdit()
        self.sid_entry.setPlaceholderText(text["Login"][4]) # "Ex: 802-12-3456
        self.sid_entry.setFont(entry_font)
        self.sid_entry.textChanged.connect(self.format_student_id)
        self.sid_entry.returnPressed.connect(self.focus_next_password)
        
        self.pass_entry = QLineEdit()
        self.pass_entry.setPlaceholderText(text["Login"][5]) # password
        self.pass_entry.setFont(entry_font)
        self.pass_entry.setEchoMode(QLineEdit.Password)
        self.pass_entry.returnPressed.connect(self.login)

        
        # Create a toggle for showing/hiding password as clickable text
        self.toggle_button = QPushButton(text["_general_boxes"][3]) # Show
        self.toggle_button.setFont(QFont('Playfair Display', 13))
        self.toggle_button.setStyleSheet("border: none; color: black; text-decoration: underline;")
        self.toggle_button.clicked.connect(self.toggle_password_visibility)
        
        # Set labels with larger font and fixed width
        user_label = QLabel(text["Login"][0]) # Username
        user_label.setFont(label_font)
        
        sid_label = QLabel(text["Login"][1]) #"Student ID"
        sid_label.setFont(label_font)
        
        pass_label = QLabel(text["Login"][2]) # "Password"
        pass_label.setFont(label_font)
        
        # Add widgets to the form layout
        form_layout.addRow(user_label, self.user_entry)
        form_layout.addRow(sid_label, self.sid_entry)
        
        # Create a layout for the password input and toggle button
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.pass_entry)
        password_layout.addWidget(self.toggle_button)
        
        form_layout.addRow(pass_label, password_layout)
        
        central_layout.addLayout(form_layout)
        
        # Create buttons
        button_layout = QHBoxLayout()  # Changed to horizontal layout
        
        self.login_button = QPushButton(text["Login"][6]) # Login
        self.login_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        self.login_button.clicked.connect(self.login)
        
        self.forgot_button = QPushButton(text["Login"][7]) #"Forgot Password"
        self.forgot_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        self.forgot_button.clicked.connect(self.on_forgot_password_click)

        self.signup_button = QPushButton(text["Login"][8]) # "Sign Up"
        self.signup_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        self.signup_button.clicked.connect(self.on_sign_up_click)
        
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.forgot_button)
        button_layout.addWidget(self.signup_button)
        
        central_layout.addLayout(button_layout)
        
        # Set maximum width for the input and button frame
        central_frame.setMaximumWidth(600)
        
        # Add the central frame to the main layout
        main_layout.addWidget(central_frame, alignment=Qt.AlignCenter)
        
        # Add a spacer to push the content upwards
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        self.setLayout(main_layout)

    def toggle_password_visibility(self):
        if self.pass_entry.echoMode() == QLineEdit.Password:
            self.pass_entry.setEchoMode(QLineEdit.Normal)
            self.toggle_button.setText(text["_general_boxes"][4]) # hide 
        else:
            self.pass_entry.setEchoMode(QLineEdit.Password)
            self.toggle_button.setText(text["_general_boxes"][3]) # show

    def login(self):
        if (verify_credentials(self.user_entry.text(), self.sid_entry.text(), self.pass_entry.text())):
            self.student_id = self.sid_entry.text()  # Store the student ID
            QMessageBox.information(self, text["Login_pop_ups"][0], text["Login_pop_ups"][1] )# "Welcome", "Login Successful")
            self.login_successful.emit()
        else:
            QMessageBox.critical(self, text["_general_boxes"][5], text["Login_pop_ups"][2]) # invalid log in
    
    def on_forgot_password_click(self):
        # Emit the signal to switch to Forgot Password screen
        self.switch_to_forgot_password.emit()

    def on_sign_up_click(self):
        self.switch_to_signup.emit()

    def reset_form(self):
        # Clear input fields
        self.user_entry.clear()
        self.sid_entry.clear()
        self.pass_entry.clear()

    def get_student_id(self):
        return self.student_id  # Return the stored student ID
    
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

    def limit_email_input(self):
        text = self.user_entry.text()

        # Regex pattern to match valid email format with a top-level domain (e.g., .com, .net, .edu)
        email_pattern = r"^[^@]+@[^@]+\.[a-zA-Z]{3,4}$"
        
        # Check if the input matches the email pattern
        if re.match(email_pattern, text):
            # If the email matches the pattern, truncate the input and prevent further typing
            self.user_entry.setMaxLength(len(text))
        else:
            # Allow further typing if the email format is not yet complete
            self.user_entry.setMaxLength(100)  # Set a reasonable max length for email input

    def focus_next_sid(self):
        """Move focus to the Student ID input when Enter is pressed in the email field."""
        if self.user_entry.hasAcceptableInput():  # Only move if the email is valid
            self.sid_entry.setFocus()

    def focus_next_password(self):
        """Move focus to the password input when Enter is pressed in the Student ID field."""
        if self.sid_entry.hasAcceptableInput():  # Only move if the Student ID is valid
            self.pass_entry.setFocus()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())
    
