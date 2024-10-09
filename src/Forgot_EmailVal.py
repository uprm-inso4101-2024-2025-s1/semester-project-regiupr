from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSignal
import re
import configparser
import mysql.connector
from sqlite3 import Error
from DB_connection import StudentsM 
import secrets
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import time

gen_token = secrets.token_hex(3).upper()  # 6-digit token
token_expiration = datetime.now() + timedelta(minutes=15)

class ForgotEmailVal(QWidget):
    switch_to_token_page = pyqtSignal()
    logout = pyqtSignal()

    def __init__(self):
        super().__init__()

        # Initialize failed attempts and lockout variables
        self.failed_attempts = 0
        self.lockout_time = None
        self.lockout_duration = 30  # 30 minutes
        self.remaining_time = None

        # Load the last lockout state (could be stored in a file or DB)
        self.load_lockout_state()

        config = configparser.ConfigParser()
        config.read('credentials/db_config.ini')
        self.db_connection = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )

        # Set window title and size
        self.setWindowTitle('Forgot Password - Email Validation')
        self.setGeometry(100, 100, 400, 300)
        
        # Create the main layout
        main_layout = QVBoxLayout()
        
        # Create the green banner
        banner = QLabel("RegiUPR Password Recovery")
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
        self.email_entry = QLineEdit()
        self.email_entry.setPlaceholderText("example.example@upr.edu")
        self.email_entry.setFont(entry_font)
        
        # Set labels with larger font and fixed width
        email_label = QLabel("Enter your registered email:")
        email_label.setFont(label_font)
        
        # Add widgets to the form layout
        form_layout.addRow(email_label, self.email_entry)
        
        central_layout.addLayout(form_layout)
        
        # Create buttons
        button_layout = QHBoxLayout()  # Changed to horizontal layout
        
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        self.submit_button.clicked.connect(self.validate_email)

        button_layout.addWidget(self.submit_button)
        
        central_layout.addLayout(button_layout)
        
        # Set maximum width for the input and button frame
        central_frame.setMaximumWidth(600)
        
        # Add the central frame to the main layout
        main_layout.addWidget(central_frame, alignment=Qt.AlignCenter)
        
        # Add a spacer to push the content upwards
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        self.setLayout(main_layout)

    def get_lockout_time(self):
        return self.lockout_time
    
    def get_remaining_time(self):
        return self.remaining_time
    
    def get_failed_attempts(self):
        return self.failed_attempts

    def send_email_with_token(self, email, username):
        # Email message format
        message = MIMEMultipart()
        message['From'] = "regiupr@gmail.com"
        message['To'] = email
        message['Subject'] = "Password Reset Token"
        
        body = f"""\
        Dear {username},

        Here is your one-time token for your password reset process: {gen_token}.

        Remember, this code is only valid for the next 15 minutes!

        If you have any further problems, please contact our support!
        """
        
        message.attach(MIMEText(body, 'plain'))

        # Send email using SMTP
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login('regiupr@gmail.com', 'your-email-password')  # Replace with your email login
                server.sendmail(message['From'], message['To'], message.as_string())
            print("Token sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
    
    def validate_email(self):
        email = self.email_entry.text()

        if self.failed_attempts >= 6:
                self.lockout_time = time.time()
                self.save_lockout_state()
                self.check_lockout()
                self.logout.emit()
        else:     
            if self.validate_email_format(email):
                self.check_email_in_db(email)
            else:
                QMessageBox.warning(self, "Error", "Invalid email format. Please enter a valid UPR email.")
                self.failed_attempts += 1
                self.save_lockout_state()
        

    def load_lockout_state(self):
        try:
            with open("lockout_state.txt", "r") as f:
                data = f.read().split(',')
                self.failed_attempts = int(data[0])
                self.lockout_time = float(data[1]) if data[1] != 'None' else None
        except FileNotFoundError:
            self.failed_attempts = 0
            self.lockout_time = None

    def save_lockout_state(self):
        with open("lockout_state.txt", "w") as f:
            f.write(f"{self.failed_attempts},{self.lockout_time}")

    def validate_email_format(self, email):
        # Regular expression to validate the email format
        pattern = r"^[a-zA-Z0-9._]+[a-zA-Z0-9]@upr\.edu$"
        return re.match(pattern, email) is not None
    
    def check_email_in_db(self, email):
        student_list = StudentsM.fetch_table(self.db_connection)
        email_found = False
        self.username = None
        for row in student_list:
            if row[2] == email:  # Check if the email matches
                email_found = True  # Set the flag to True if a match is found
                self.username = row[1]
                global stu_id 
                stu_id = row[0]
                break  # Exit the loop if a match is found

        # After the loop, check the flag to show the appropriate message
        if email_found:
            QMessageBox.information(self, "Success", "Email found! You can proceed with recovery.")
            #self.send_email_with_token(email, username) //Send email
            self.failed_attempts = 0
            self.lockout_time = None
            self.save_lockout_state()
            print(gen_token)
            token_expiration = datetime.now() + timedelta(minutes=15)
            print(token_expiration)
            self.switch_to_token_page.emit()
        else:
            QMessageBox.warning(self, "Email Not Found", "No account associated with this email.")
            self.failed_attempts += 1
            self.save_lockout_state()
   
    def check_lockout(self):
        if self.lockout_time is not None:
            elapsed_time = time.time() - self.lockout_time
            if elapsed_time < self.lockout_duration * 60:
                remaining_time = self.lockout_duration * 60 - elapsed_time
                QMessageBox.warning(self, "Locked Out", f"Please try again in {int(remaining_time // 60)} minutes.")
            else:
                # Reset after 30 minutes
                self.failed_attempts = 0
                self.lockout_time = None
                self.save_lockout_state()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ForgotEmailVal()
    window.show()
    sys.exit(app.exec_())
    