from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSignal
import configparser
import mysql.connector
from Forgot_EmailVal import *
from Forgot_EmailVal import ForgotEmailVal as ForgotScreen
from Reset_TokenVal import TokenValidation as TokenScreen
import hashlib

class NewPass(QWidget):

    logout = pyqtSignal()         # Signal emitted to log out

    def __init__(self, forgot_email_screen):
        super().__init__()

        self.forgot_email_screen = forgot_email_screen
        self.token_screen = TokenScreen

        config = configparser.ConfigParser()
        config.read('credentials/db_config.ini')
        self.db_connection = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )

        self.setWindowTitle("Forgot Password - Set New Password")
        self.setGeometry(100, 100, 800, 600)  # Set a default size for the window
        self.setWindowState(Qt.WindowMaximized)  # Start maximized
        
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
        self.new_pass = QLineEdit()
        self.new_pass.setPlaceholderText("New Password Here")
        self.new_pass.setFont(entry_font)
        self.new_pass.setEchoMode(QLineEdit.Password)
        self.new_pass.returnPressed.connect(self.focus_next_confirm)
        
        self.confirm_pass = QLineEdit()
        self.confirm_pass.setPlaceholderText("password")
        self.confirm_pass.setFont(entry_font)
        self.confirm_pass.setEchoMode(QLineEdit.Password)
        self.confirm_pass.returnPressed.connect(self.submit_password)
        
        # Create a toggle for showing/hiding password as clickable text
        self.toggle_button = QPushButton("Show")
        self.toggle_button.setFont(QFont('Playfair Display', 13))
        self.toggle_button.setStyleSheet("border: none; color: black; text-decoration: underline;")
        self.toggle_button.clicked.connect(self.toggle_password_visibility)
        
        # Set labels with larger font and fixed width
        new_label = QLabel("Enter New Password:")
        new_label.setFont(label_font)
        
        confirm_label = QLabel("Confirm New Password:")
        confirm_label.setFont(label_font)
    
        # Create a layout for the password input and toggle button
        newpass_layout = QHBoxLayout()
        newpass_layout.addWidget(self.new_pass)
        newpass_layout.addWidget(self.toggle_button)
        
        form_layout.addRow(new_label, newpass_layout)

        confirm_layout = QHBoxLayout()
        confirm_layout.addWidget(self.confirm_pass)
        confirm_layout.addWidget(self.toggle_button)
        
        form_layout.addRow(confirm_label, confirm_layout)
        
        central_layout.addLayout(form_layout)
        
        # Create buttons
        button_layout = QHBoxLayout()  # Changed to horizontal layout
        
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        self.confirm_button.clicked.connect(self.submit_password)

        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        self.cancel_button.clicked.connect(self.cancel)
        
        button_layout.addWidget(self.confirm_button)
        button_layout.addWidget(self.cancel_button)
        
        central_layout.addLayout(button_layout)
        
        # Set maximum width for the input and button frame
        central_frame.setMaximumWidth(600)
        
        # Add the central frame to the main layout
        main_layout.addWidget(central_frame, alignment=Qt.AlignCenter)
        
        # Add a spacer to push the content upwards
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        self.setLayout(main_layout)

    def toggle_password_visibility(self):
        if self.new_pass.echoMode() == QLineEdit.Password and self.confirm_pass.echoMode() == QLineEdit.Password:
            self.new_pass.setEchoMode(QLineEdit.Normal)
            self.confirm_pass.setEchoMode(QLineEdit.Normal)
            self.toggle_button.setText("Hide")
        else:
            self.new_pass.setEchoMode(QLineEdit.Password)
            self.confirm_pass.setEchoMode(QLineEdit.Password)
            self.toggle_button.setText("Show")
    
    def submit_password(self):
        new_password = self.new_pass.text()
        confirm_password = self.confirm_pass.text()

        if new_password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match. Please try again.")
            return

        # If passwords match, proceed to update in the database
        self.update_password_in_db(new_password)

    def update_password_in_db(self, new_password):
        self.db_cursor = self.db_connection.cursor()
        self.stu_id = self.forgot_email_screen.get_stu_id()  # Retrieve the student ID
        if not self.stu_id:
            QMessageBox.warning(self, "Error", "Student ID not found.")
            return
        # Debugging prints to check values
        print(f"Student ID: {self.stu_id}")
        print(f"New Password: {new_password}")
        # Update the password for the user in the database
        self.db_cursor.execute("UPDATE `students` SET `password` = %s WHERE `student_id` = %s", (new_password, self.stu_id))
        self.db_connection.commit()

        QMessageBox.information(self, "Success", "Password updated successfully.")
        StudentsM.fetch_table(self.db_connection)
        self.logout.emit()
        self.db_connection.close()

    def cancel(self):
        reply = QMessageBox.question(self, 'Cancel Password Recovery',
                                     "Are you sure you want to cancel?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.new_pass.setText("")
            self.confirm_pass.setText("")
            self.forgot_email_screen.reset_email_entry
            self.token_screen.reset_token_entry
            self.logout.emit()
    
    def focus_next_confirm(self):
        """Move focus to the Student ID input when Enter is pressed in the email field."""
        if len(self.new_pass.text()) > 0:  # Only move if the email is valid
            self.confirm_pass.setFocus()
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = NewPass()
    window.show()
    sys.exit(app.exec_())
    