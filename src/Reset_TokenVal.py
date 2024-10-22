from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from datetime import datetime
from Forgot_EmailVal import ForgotEmailVal as ForgotScreen
import re


class TokenValidation(QWidget):

    switch_to_newpass = pyqtSignal(object) # Signal emitted to new pass
    logout = pyqtSignal()

    def __init__(self, generated_token, token_expiration, forgot_email_screen):
        super().__init__()

        self.forgot_email_screen = forgot_email_screen
        self.generated_token = generated_token
        self.token_expiration = token_expiration

        # Set window title and size
        self.setWindowTitle('Forgot Password - Token Validation')
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
        self.token_input = QLineEdit(self)
        self.token_input.textChanged.connect(self.convert_to_uppercase)
        self.token_input.setPlaceholderText("xxxxxx")
        self.token_input.setFont(entry_font)
        self.token_input.returnPressed.connect(self.validate_token)
        self.token_input.textChanged.connect(self.limit_token_input)
        
        # Set labels with larger font and fixed width
        token_label = QLabel("Enter your one-time token:")
        token_label.setFont(label_font)
        
        # Add widgets to the form layout
        form_layout.addRow(token_label, self.token_input)
        
        central_layout.addLayout(form_layout)
        
        # Create buttons
        button_layout = QHBoxLayout()  # Changed to horizontal layout
        
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        self.submit_button.clicked.connect(self.validate_token)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("background-color: #D3D3D3; color: black; font-size: 10pt; padding: 10px; border: 2px solid black;")
        self.cancel_button.clicked.connect(self.cancel)

        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.cancel_button)
        
        central_layout.addLayout(button_layout)
        
        # Set maximum width for the input and button frame
        central_frame.setMaximumWidth(600)
        
        # Add the central frame to the main layout
        main_layout.addWidget(central_frame, alignment=Qt.AlignCenter)
        
        # Add a spacer to push the content upwards
        main_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        self.setLayout(main_layout)

    def validate_token(self):
        entered_token = self.token_input.text()

        # Check if token is expired
        if datetime.now() > self.token_expiration:
            QMessageBox.warning(self, "Token Expired", "The token has expired. Please try again.")
            return

        # Check if the entered token matches the generated one
        if entered_token == self.generated_token:
            QMessageBox.information(self, "Success", "Token validated successfully! Proceed with password reset.")
            self.switch_to_newpass.emit(self.forgot_email_screen)
            # Redirect to password reset page or functionality
        else:
            QMessageBox.warning(self, "Invalid Token", "The entered token is incorrect. Please try again.")

    def convert_to_uppercase(self):
        # Convert input text to uppercase
        current_text = self.token_input.text()
        self.token_input.setText(current_text.upper())

    def cancel(self):
        reply = QMessageBox.question(self, 'Cancel Password Recovery',
                                     "Are you sure you want to cancel?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.token_input.clear()
            self.forgot_email_screen.reset_email_entry
            self.logout.emit()

    def reset_token_entry(self):
        self.token_input.setText("")

    def limit_token_input(self):
        text = self.token_input.text()  # Replace with the relevant QLineEdit input field

        # Allow only alphanumeric characters (letters and digits)
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text)
        
        # Limit input to 6 characters
        if len(cleaned_text) > 6:
            cleaned_text = cleaned_text[:6]
        
        # Update the input field without affecting the cursor position
        self.token_input.blockSignals(True)  # Prevent triggering textChanged again
        self.token_input.setText(cleaned_text)
        self.token_input.blockSignals(False)