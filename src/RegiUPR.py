import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget
from Login import Login
from Main_Menu import MainMenu
from Profile import Profile

class RegiUPRApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Initialize the pages
        self.login_page = Login()
        self.main_menu_page = MainMenu()
        self.profile_page = Profile()
         
        # Add pages to the stacked widget
        self.addWidget(self.login_page)
        self.addWidget(self.main_menu_page)
        self.addWidget(self.profile_page)

        # Connect signals
        self.login_page.login_successful.connect(self.show_main_menu)
        self.main_menu_page.view_profile.connect(self.show_profile)
        self.main_menu_page.logout.connect(self.show_login)
        self.profile_page.view_main_menu.connect(self.show_main_menu)
        self.profile_page.logout.connect(self.show_login)

        # Start with the login page
        self.setCurrentWidget(self.login_page)

        # Maximize the window when the application starts
        self.showMaximized()

    def show_login(self):
        self.login_page.reset_form()
        self.setCurrentWidget(self.login_page)

    def show_main_menu(self):
        self.setCurrentWidget(self.main_menu_page)

    def show_profile(self):
        self.setCurrentWidget(self.profile_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegiUPRApp()
    window.setWindowTitle("RegiUPR")
    window.show()
    sys.exit(app.exec_())
