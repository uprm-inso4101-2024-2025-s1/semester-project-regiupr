from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSignal

from Login_backend import start_login, verify_credentials

class Login(QWidget):
    login_successful = pyqtSignal()  # Signal emitted on successful login

    def __init__(self):
        super().__init__()

        start_login()
        self.setWindowTitle("Login to RegiUPR")
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
        
        # Create input widgets with placeholder text
        self.user_entry = QLineEdit()
        self.user_entry.setPlaceholderText("Ex: student.name@upr.edu")
        self.user_entry.setFont(entry_font)
        
        self.sid_entry = QLineEdit()
        self.sid_entry.setPlaceholderText("Ex: 802-12-3456")
        self.sid_entry.setFont(entry_font)
        
        self.pass_entry = QLineEdit()
        self.pass_entry.setPlaceholderText("password")
        self.pass_entry.setFont(entry_font)
        self.pass_entry.setEchoMode(QLineEdit.Password)
        
        # Create a toggle for showing/hiding password as clickable text
        self.toggle_button = QPushButton("Show")
        self.toggle_button.setFont(QFont('Playfair Display', 13))
        self.toggle_button.setStyleSheet("border: none; color: black; text-decoration: underline;")
        self.toggle_button.clicked.connect(self.toggle_password_visibility)
        
        # Set labels with larger font and fixed width
        user_label = QLabel("Username")
        user_label.setFont(label_font)
        
        sid_label = QLabel("Student ID")
        sid_label.setFont(label_font)
        
        pass_label = QLabel("Password")
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
        
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        self.login_button.clicked.connect(self.login)
        
        self.cant_button = QPushButton("Can't Login")
        self.cant_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.cant_button)
        
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
            self.toggle_button.setText("Hide")
        else:
            self.pass_entry.setEchoMode(QLineEdit.Password)
            self.toggle_button.setText("Show")

    def login(self):
        if (verify_credentials(self.user_entry.text(), self.sid_entry.text(), self.pass_entry.text())):
            self.student_id = self.sid_entry.text()  # Store the student ID
            QMessageBox.information(self, "Welcome", "Login Successful")
            self.login_successful.emit()
        else:
            QMessageBox.critical(self, "Error", "Invalid Login")
    
    def reset_form(self):
        # Clear input fields
        self.user_entry.clear()
        self.sid_entry.clear()
        self.pass_entry.clear()

    def get_student_id(self):
        return self.student_id  # Return the stored student ID

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())
