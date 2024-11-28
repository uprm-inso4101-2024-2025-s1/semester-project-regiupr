import sys
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMenu
from PyQt5.QtGui import QIcon
from Login import Login
from Main_Menu import MainMenu
from Profile import Profile
from Course_Enrollment import CourseEnroll
from Forgot_EmailVal import ForgotEmailVal
from Forgot_EmailVal import gen_token, token_expiration
from Reset_TokenVal import TokenValidation
from New_Pass import NewPass
from Sign_Up import SignUp
from gui_backend.Login_backend import *
#Language
from Language import parse_UI_content_string_document, lang_path, set_current_language

class RegiUPRApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        #LANG
        parse_UI_content_string_document(lang_path)

        # Initialize the pages
        self.login_page = Login()
        self.main_menu_page = None
        self.profile_page = None
        self.course_enroll_page = CourseEnroll()
        self.forgot_email_screen = ForgotEmailVal() 
        self.token_screen = TokenValidation(gen_token, token_expiration, self.forgot_email_screen)
        self.newpass_screen = NewPass(self.forgot_email_screen)
        self.signup_screen = SignUp()
        self.test = None
         
        # Add pages to the stacked widget
        self.addWidget(self.login_page)
        #self.addWidget(self.main_menu_page)
        #self.addWidget(self.profile_page)
        #self.addWidget(self.course_enroll_page)
        self.addWidget(self.forgot_email_screen)
        self.addWidget(self.token_screen)
        self.addWidget(self.newpass_screen)
        self.addWidget(self.signup_screen)


        # Connect signals
        self.login_page.login_successful.connect(self.show_main_menu)
        #self.main_menu_page.view_profile.connect(self.show_profile)
        #self.main_menu_page.view_courses.connect(self.show_course_enroll)
        #self.main_menu_page.logout.connect(self.show_login)
        
        # if self.profile_page is not None:
        #     self.profile_page.view_main_menu.connect(self.show_main_menu)
        #     self.profile_page.view_courses.connect(self.show_course_enroll)
        #     self.profile_page.logout.connect(self.show_login)
        self.course_enroll_page.view_main_menu.connect(self.show_main_menu)
        self.course_enroll_page.view_profile.connect(self.show_profile)
        self.course_enroll_page.logout.connect(self.show_login)
        self.login_page.switch_to_forgot_password.connect(self.show_forgot_email_screen)
        self.forgot_email_screen.switch_to_token_page.connect(self.show_token_screen)
        self.token_screen.switch_to_newpass.connect(self.show_newpass)
        self.newpass_screen.logout.connect(self.show_login)
        self.forgot_email_screen.logout.connect(self.show_login)
        self.token_screen.logout.connect(self.show_login)
        self.login_page.switch_to_signup.connect(self.show_signup)
        self.signup_screen.logout.connect(self.show_login)

        # Setup language button and main layout
        self.setup_language_button()

        # Start with the login page
        self.setCurrentWidget(self.login_page)

        # Maximize the window when the application starts
        self.showMaximized()

    def setup_language_button(self):
        # Create main container widget
        self.main_widget = QWidget()
        layout = QVBoxLayout(self.main_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Add the QStackedWidget as main content
        layout.addWidget(self)

        # Create language button
        self.language_button = QPushButton()
        self.language_button.setStyleSheet("background-color: transparent; color: black; font-size: 14px;")
        self.language_button.setFixedSize(80, 80)
        self.language_button.setIcon(QIcon("src/resources/flags/usa_flag.png"))
        self.language_button.setIconSize(QSize(150, 80))

        # Create dropdown menu
        language_menu = QMenu()
        language_menu.addAction("English", lambda: self.set_language("English"))
        language_menu.addAction("Español", lambda: self.set_language("Español"))
        self.language_button.setMenu(language_menu)

        # Create container for button positioning
        button_container = QHBoxLayout()
        button_container.addStretch()
        button_container.addWidget(self.language_button)

        # Button spacing from floor and right corner
        button_container.setContentsMargins(0, 0, 20, 20)

        layout.addLayout(button_container)
    
    def hide_language_button(self):
        self.language_button.setVisible(False)  # Button invisible

    def show_language_button(self):
        self.language_button.setVisible(True)  # Button visble

    def set_language(self, language):
        if language == "English":
            self.language_button.setIcon(QIcon("src/resources/flags/usa_flag.png"))
            set_current_language("english")
            self.reload_page()
            print("Language set to English")
        elif language == "Español":
            self.language_button.setIcon(QIcon("src/resources/flags/pr_flag.png"))
            set_current_language("spanish")
            self.reload_page()
            print("Idioma cambiado a Español")
        
        # Update UI elements with new language
        # self.update_ui_language()

    def reload_page(self):
        # Update all pages with new language
        if self.login_page:
            self.login_page.refresh_page()
        # if self.main_menu_page:
        #     self.main_menu_page.refresh_page()
        # if self.profile_page:
        #     self.profile_page.refresh_page()
        # if self.course_enroll_page:
        #     self.course_enroll_page.refresh_page()
        # Add other pages as needed

    # Rest of the existing methods remain the same
    def show_login(self):
        self.profile_page = None
        self.main_menu_page = None
        self.login_page.reset_form()
        self.setCurrentWidget(self.login_page)
        self.show_language_button()

    def create_main_menu(self):
        if self.main_menu_page is None:
            self.main_menu_page = MainMenu()  # Initialize MainMenu
            self.addWidget(self.main_menu_page)  # Add it to the stack if it's not already added
            
            # Connect signals after initializing MainMenu
            self.main_menu_page.view_profile.connect(self.show_profile)
            self.main_menu_page.view_courses.connect(self.show_course_enroll)
            self.main_menu_page.logout.connect(self.show_login)

    def reload_page2(self):
        if self.profile_page is None:
            self.removeWidget(self.login_page)
            self.login_page = None 
            self.login_page = Login()
            self.addWidget(self.login_page)
            self.login_page.login_successful.connect(self.show_main_menu)
            self.login_page.switch_to_forgot_password.connect(self.show_forgot_email_screen)
            self.login_page.switch_to_signup.connect(self.show_signup)
            self.show_login()
        elif 1:
            pass

    def show_main_menu(self):
        if self.main_menu_page is None:
            self.create_main_menu()

        # WE HAVE to initiaize the profile screen even if it isn't being show because if not, when pressed 
        # at first, there a delay. Now, if initialized here, that delay is covered by the time lapse of the
        # successful login pop up.
        if self.profile_page is None:
            self.create_profile()

        self.setCurrentWidget(self.main_menu_page)
        self.hide_language_button()


    def create_profile(self):
        if self.profile_page is None:
            self.profile_page = Profile()
            self.addWidget(self.profile_page)

            self.profile_page.view_main_menu.connect(self.show_main_menu)
            self.profile_page.view_courses.connect(self.show_course_enroll)
            self.profile_page.logout.connect(self.show_login)

    def show_profile(self):
        if self.profile_page is None:
            self.create_profile()

        self.setCurrentWidget(self.profile_page)
        self.show_language_button()

    def show_course_enroll(self):
        self.setCurrentWidget(self.course_enroll_page)
        self.hide_language_button()

    def show_forgot_email_screen(self):
        self.setCurrentWidget(self.forgot_email_screen)
        self.hide_language_button()
    
    def show_token_screen(self):
        self.setCurrentWidget(self.token_screen)
        self.hide_language_button()
    
    def show_newpass(self):
        self.setCurrentWidget(self.newpass_screen)
        self.hide_language_button()

    def show_signup(self):
        self.setCurrentWidget(self.signup_screen)
        self.hide_language_button()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegiUPRApp()
    window.setWindowTitle("RegiUPR")
    window.main_widget.showMaximized() # Show the main widget instead of the window directly
    
    sys.exit(app.exec_())