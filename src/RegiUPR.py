import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget
from Login import Login
from Main_Menu import MainMenu
from Profile import Profile
from Course_Enrollment import CourseEnroll
from college_planning import CollegePlanning
from Forgot_EmailVal import ForgotEmailVal
from Forgot_EmailVal import gen_token, token_expiration
from Reset_TokenVal import TokenValidation
from New_Pass import NewPass
from Sign_Up import SignUp
from Confirm_Taken import ConfirmTaken
from gui_backend.Login_Backend import *

class RegiUPRApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Initialize the pages
        self.login_page = Login()
        self.main_menu_page = None
        self.profile_page = None
        self.course_enroll_page = None
        self.college_planning_page = None
        self.forgot_email_screen = ForgotEmailVal() 
        self.token_screen = TokenValidation(gen_token, token_expiration, self.forgot_email_screen)
        self.newpass_screen = NewPass(self.forgot_email_screen)
        self.signup_screen = SignUp()
        self.course_selec = None  # Initialize course selection as None
         
        # Add pages to the stacked widget
        self.addWidget(self.login_page)
        #self.addWidget(self.main_menu_page)
        #self.addWidget(self.profile_page)
        #self.addWidget(self.course_enroll_page)
        self.addWidget(self.forgot_email_screen)
        self.addWidget(self.token_screen)
        self.addWidget(self.newpass_screen)
        self.addWidget(self.signup_screen)
        #self.addWidget(self.course_selec)


        # Connect signals
        self.login_page.login_successful.connect(self.show_main_menu)
        #self.main_menu_page.view_profile.connect(self.show_profile)
        #self.main_menu_page.view_courses.connect(self.show_course_enroll)
        #self.main_menu_page.logout.connect(self.show_login)
        
        # if self.profile_page is not None:
        #     self.profile_page.view_main_menu.connect(self.show_main_menu)
        #     self.profile_page.view_courses.connect(self.show_course_enroll)
        #     self.profile_page.logout.connect(self.show_login)
        #self.course_enroll_page.view_main_menu.connect(self.show_main_menu)
        #self.course_enroll_page.view_profile.connect(self.show_profile)
        #self.course_enroll_page.logout.connect(self.show_login)
        self.login_page.switch_to_forgot_password.connect(self.show_forgot_email_screen)
        self.forgot_email_screen.switch_to_token_page.connect(self.show_token_screen)
        self.token_screen.switch_to_newpass.connect(self.show_newpass)
        self.newpass_screen.logout.connect(self.show_login)
        self.forgot_email_screen.logout.connect(self.show_login)
        self.token_screen.logout.connect(self.show_login)
        self.login_page.switch_to_signup.connect(self.show_signup)
        self.signup_screen.logout.connect(self.show_login)
        self.signup_screen.courses.connect(self.show_course_selection)

        # Start with the login page
        self.setCurrentWidget(self.login_page)

        # Maximize the window when the application starts
        self.showMaximized()


    def show_login(self):
        self.profile_page = None
        self.main_menu_page = None
        self.login_page.reset_form()
        self.setCurrentWidget(self.login_page)

    def create_main_menu(self):
        if self.main_menu_page is None:
            self.main_menu_page = MainMenu()  # Initialize MainMenu
            self.addWidget(self.main_menu_page)  # Add it to the stack if it's not already added
            
            # Connect signals after initializing MainMenu
            self.main_menu_page.view_profile.connect(self.show_profile)
            self.main_menu_page.view_courses.connect(self.show_course_enroll)
            self.main_menu_page.view_college_planning.connect(self.show_college_planning)
            self.main_menu_page.logout.connect(self.show_login)
            print("Main menu created and signals connected.")  # Debug

    


    def show_main_menu(self):
        if self.main_menu_page is None:
            self.create_main_menu()
        # Refresh the data for the main menu each time it is shown
        self.main_menu_page.update_ui_for_semester()  # Assuming you create this method to refresh the content

        # WE HAVE to initiaize the profile screen even if it isn't being show because if not, when pressed 
        # at first, there a delay. Now, if initialized here, that delay is covered by the time lapse of the
        # successful login pop up.
        if self.profile_page is None:
            self.create_profile()

        if self.course_enroll_page is None:
            self.create_course_enroll()

        if self.college_planning_page is None:
            self.create_college_planning()

        self.setCurrentWidget(self.main_menu_page)

    def create_profile(self):
        if self.profile_page is None:
            self.profile_page = Profile()
            self.addWidget(self.profile_page)

            self.profile_page.view_main_menu.connect(self.show_main_menu)
            self.profile_page.view_college_planning.connect(self.show_college_planning)
            self.profile_page.view_courses.connect(self.show_course_enroll)
            self.profile_page.logout.connect(self.show_login)

    def show_profile(self):
        if self.profile_page is None:
            self.create_profile()

        self.setCurrentWidget(self.profile_page)

    def create_course_enroll(self):
        if self.course_enroll_page is None:
            self.course_enroll_page = CourseEnroll()
            self.addWidget(self.course_enroll_page)

            self.course_enroll_page.view_main_menu.connect(self.show_main_menu)
            self.course_enroll_page.view_college_planning.connect(self.show_college_planning)
            self.course_enroll_page.view_profile.connect(self.show_profile)
            self.course_enroll_page.logout.connect(self.show_login)

    def show_course_enroll(self):
        if self.course_enroll_page is None:
            self.create_course_enroll()
        
        self.setCurrentWidget(self.course_enroll_page)

    def create_college_planning(self):
        if self.college_planning_page is None:
            print("Creating College Planning page...")  # Debug

            self.college_planning_page = CollegePlanning()
            self.addWidget(self.college_planning_page)

            self.college_planning_page.view_profile.connect(self.show_profile)
            self.college_planning_page.view_courses.connect(self.show_course_enroll)
            self.college_planning_page.view_main_menu.connect(self.show_main_menu)
            self.college_planning_page.logout.connect(self.show_login)
            print("College Planning page created.")  # Debug


    def show_college_planning(self):
        print("Switching to College Planning page...")  # Debug
        if self.college_planning_page is None:
            self.create_college_planning()

        self.setCurrentWidget(self.college_planning_page)
        print("College Planning page displayed.")  # Debug


    def show_forgot_email_screen(self):
        self.setCurrentWidget(self.forgot_email_screen)
    
    def show_token_screen(self):
        self.setCurrentWidget(self.token_screen)
    
    def show_newpass(self):
        self.setCurrentWidget(self.newpass_screen)

    def show_signup(self):
        self.setCurrentWidget(self.signup_screen)

    def show_course_selection(self, student_id, curriculum_id):
        if self.course_selec is None:
            # Pass necessary parameters to ConfirmTaken
            student_id = self.signup_screen.student_id
            curriculum_id = self.signup_screen.curriculum_id
            current_semester = self.signup_screen.current_semester

            # Initialize ConfirmTaken with correct parameters
            self.course_selec = ConfirmTaken(student_id, curriculum_id, current_semester)
            self.addWidget(self.course_selec)
            # Connect signals
            self.course_selec.selection_complete.connect(self.show_login)
            self.course_selec.switch_to_signup.connect(self.show_signup)
        self.setCurrentWidget(self.course_selec)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegiUPRApp()
    window.setWindowTitle("RegiUPR")
    window.show()
    
    sys.exit(app.exec_())
