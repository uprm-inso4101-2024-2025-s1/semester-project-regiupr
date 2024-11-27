import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, 
                             QTableWidgetItem, QPushButton, QHBoxLayout, QGridLayout, QDialog, QMessageBox, QSpacerItem)
from PyQt5.QtGui import QFont, QColor, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from Main_Menu import MainMenu
from gui_backend import Course_Eligibility, db_connection, Profile_Backend, Login_Backend

class SemesterTableWidget(QTableWidget):
    def __init__(self, semester_name, student_id, conn, parent=None):
        super().__init__(parent)
        self.semester_name = semester_name
        self.student_id = student_id
        self.conn = conn
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)

    def dropEvent(self, event):
        if event.source() and isinstance(event.source(), QtWidgets.QListWidget):
            dragged_item = event.source().currentItem()
            course_code = dragged_item.text()

            cursor = self.conn.cursor()
            try:
                planning_id = self.get_or_create_planning_id(cursor)
                self.add_course_to_planned_courses(planning_id, course_code, cursor)

                # Add to UI
                row = self.rowCount()
                self.insertRow(row)
                self.setItem(row, 0, QTableWidgetItem(course_code))
                self.setItem(row, 1, QTableWidgetItem(dragged_item.toolTip()))

                event.accept()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to plan course: {e}")
                event.ignore()
            finally:
                cursor.close()
    
    def get_or_create_planning_id(self, cursor):
        query_check = """
        SELECT planning_id FROM semester_planning
        WHERE student_id = %s AND semester_name = %s
        """
        cursor.execute(query_check, (self.student_id, self.semester_name))
        result = cursor.fetchone()

        if result:
            return result[0]

        # Create new planning_id
        planning_id = QtCore.QUuid.createUuid().toString()
        query_insert = """
        INSERT INTO semester_planning (planning_id, student_id, semester_name)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query_insert, (planning_id, self.student_id, self.semester_name))
        self.conn.commit()
        return planning_id

    def add_course_to_planned_courses(self, planning_id, course_code, cursor):
        query_insert = """
        INSERT INTO planned_courses (planning_id, course_code)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE course_code = course_code
        """
        cursor.execute(query_insert, (planning_id, course_code))
        self.conn.commit()

class CollegePlanning(QWidget):
    view_profile = pyqtSignal()  # Signal emitted to view profile
    view_main_menu = pyqtSignal() # Signal emitted to view Main Menu
    logout = pyqtSignal()        # Signal emitted to log out
    view_courses = pyqtSignal()  # Signal emitted to view Course Enrollment

    def __init__(self):
        super().__init__()
        print("Initializing CollegePlanning screen...")  # Debug

        student_data = Profile_Backend.get_student_data(Login_Backend.get_student_info()) # ****** <-- UNCOMMENT WHEN DOING FULL INTEGRATION WITH APP
        self.student_id = student_data["student_id"]
        self.conn = db_connection.create_connection()

        self.initUI()

        self.populate_not_taken_courses(self.student_id)
        self.populate_taken_courses(self.student_id)
        
    def initUI(self):
        # Main Layout
        main_layout = QHBoxLayout()

        # Left panel (green)
        left_panel = QWidget()
        left_panel_layout = QVBoxLayout()
        left_panel.setStyleSheet("background-color: #4CAF50;")

        # Adding Logo as an Image
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
            left_panel_layout.setContentsMargins(10, 10, 10, 10)  # Adjust margins (left, top, right, bottom)
            left_panel_layout.setSpacing(2)  # Reduce vertical spacing between buttons

        left_panel.setLayout(left_panel_layout)
        left_panel.setFixedWidth(200)

        # Connect button clicks to their respective slots
        self.btn_profile.clicked.connect(self.handle_profile)
        self.btn_logout.clicked.connect(self.confirm_logout)
        self.btn_main_menu.clicked.connect(self.handle_main_menu)
        self.btn_course_enroll.clicked.connect(self.handle_courses)

        # Center panel (Content)
        center_panel = QtWidgets.QWidget()
        self.setupUi(center_panel)  # Properly set up the layout of the center panel
        
        # Add the layout to the center panel (make sure it's added only once)
        center_panel.setLayout(self.horizontalLayout_2)

        # Centering the content by adding spacers around the center panel
        left_spacer = QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        right_spacer = QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        main_layout.addWidget(left_panel)  # Add the left panel first
        main_layout.addItem(left_spacer)   # Left spacer for centering
        main_layout.addWidget(center_panel)  # Add the center panel to the main layout
        # main_layout.addWidget(self.create_legend())  # Add legend to the main layout
        main_layout.addItem(right_spacer)  # Right spacer for centering
        
        # Set the main layout
        self.setLayout(main_layout)
        self.setWindowTitle("RegiUPR")
        self.setGeometry(100, 100, 1200, 800)

        # # Add "Add Semester" button
        # self.btn_add_semester = QPushButton("Add Semester")
        # self.btn_add_semester.setStyleSheet(button_style)
        # self.btn_add_semester.setFixedSize(170, 50)
        # self.btn_add_semester.clicked.connect(self.add_new_semester)
        # left_panel_layout.addWidget(self.btn_add_semester, alignment=Qt.AlignTop)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1098, 869)
        Form.setAutoFillBackground(False)
        
        self.widget = QtWidgets.QWidget(Form)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.widget.setObjectName("widget")
        
        ### Layout Containing the three vertical layouts
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        ### Layout Containing Planner Widget
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setObjectName("verticalLayout")
        
        ### Planner Widget
        self.PlannerLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PlannerLabel.setFont(font)
        self.PlannerLabel.setScaledContents(False)
        self.PlannerLabel.setObjectName("PlannerLabel")
        self.verticalLayout.addWidget(self.PlannerLabel)
        
        ### Tab Widget inside planner
        self.plannerTabwidget = QtWidgets.QTabWidget(self.widget)
        self.plannerTabwidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.plannerTabwidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.plannerTabwidget.setUsesScrollButtons(True)
        self.plannerTabwidget.setObjectName("plannerTabwidget")
        self.verticalLayout.addWidget(self.plannerTabwidget)
        
        ### Create tabs and semester tables
        # self.addTab("tab_1", "1", "Primer AÃ±o ")
        # self.semesterTableWidget(self.tab)
        # self.addTab("tab_2", "2", "Segundo AÃ±o ")
        # self.semesterTableWidget(self.tab)
        # self.addTab("tab_3", "3", "Tercer AÃ±o ")
        # self.semesterTableWidget(self.tab)        
        # self.addTab("tab_4", "4", "Cuarto AÃ±o ")
        # self.semesterTableWidget(self.tab)
        # self.addTab("tab_5", "5", "Quinto AÃ±o ")  
        # self.semesterTableWidget(self.tab)
        # self.addTab("tab_1", "1", "First Semester")
        # self.addTab("tab_2", "2", "Second Semester")

        cursor = self.conn.cursor()
        try:
            query = "SELECT semester_name FROM semester_planning WHERE student_id = %s"
            cursor.execute(query, (self.student_id,))
            semesters = cursor.fetchall()
            for index, (semester_name,) in enumerate(semesters, start=1):
                self.addTab(f"tab_{index}", str(index), semester_name)
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to fetch semesters: {e}")
        finally:
            cursor.close()

        self.horizontalLayout_2.addLayout(self.verticalLayout)
        
        ### Add spacer
        spacerItem = QtWidgets.QSpacerItem(400, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        
        ### Add overview button
        self.overviewButton = QtWidgets.QPushButton(self.widget)
        self.overviewButton.setObjectName("overviewButton")
        self.verticalLayout.addWidget(self.overviewButton)
        
        ### Create Horizontal Layout that contains GPA and credit trackers
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        ### GPA tracker label
        self.label = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(76, 175, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        
        ### Credit Tracker Label
        self.label_2 = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(76, 175, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        self.label_2.setPalette(palette)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        
        ### Add trackers to vlayout 1
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        ### Add vlayout1 to bigger hlayout
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        
        ### Create vlayout2 containing Available Course Widget
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        ### Available courses label
        self.availableCourses = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.availableCourses.setFont(font)
        self.availableCourses.setScaledContents(False)
        self.availableCourses.setObjectName("availableCourses")
        self.verticalLayout_2.addWidget(self.availableCourses)
        
        ### Available course list widget
        self.availCourselist = QtWidgets.QListWidget(self.widget)
        self.availCourselist.setDragEnabled(True)
        self.availCourselist.setDragDropOverwriteMode(True)
        self.availCourselist.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.availCourselist.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.availCourselist.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.availCourselist.setMovement(QtWidgets.QListView.Free)
        self.availCourselist.setResizeMode(QtWidgets.QListView.Adjust)
        self.availCourselist.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.availCourselist.setUniformItemSizes(True)
        self.availCourselist.setObjectName("availCourselist")
        
        ### Add list widget to vlayout2
        self.verticalLayout_2.addWidget(self.availCourselist)
        ### Add vlayout2 to bigger hlayout2
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        
        ### Create vlayout3 containing Taken courses
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.retranslateUi(Form)
        self.plannerTabwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Course Planner"))
        self.PlannerLabel.setText(_translate("Form", "Planner"))
        self.overviewButton.setText(_translate("Form", "Overview"))
        self.label.setText(_translate("Form", "GPA Tracker"))
        self.label_2.setText(_translate("Form", "Credit Tracker"))
        self.availableCourses.setText(_translate("Form", "Available Courses"))
        self.availCourselist.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))

    def addTab(self, objectname, display, semester_name):
        # self.tab = QtWidgets.QWidget()
        # self.tab.setObjectName(objectname)
        # self.plannerTabwidget.addTab(self.tab, display)
        # self.plannerTabwidget.setTabToolTip(self.plannerTabwidget.indexOf(self.tab), tooltip)
        
        tab = QtWidgets.QWidget()
        tab.setObjectName(objectname)

        # Create the table for the semester
        table = SemesterTableWidget(semester_name, self.student_id, self.conn, tab)
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Course Code", "Details"])
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Populate table with courses from the database
        self.populate_courses_in_semester(table, semester_name)

        layout = QVBoxLayout()
        layout.addWidget(table)
        tab.setLayout(layout)

        self.plannerTabwidget.addTab(tab, display)

    def semesterTableWidget(self, tab):
        # Create the semester table widget
        self.semesterTable = QtWidgets.QTableWidget(self.tab)
        self.semesterTable.setGeometry(QtCore.QRect(0, 0, 400, 311))  # Increase the width from 400 to 500
        self.semesterTable.setAcceptDrops(True)
        self.semesterTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.semesterTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.semesterTable.setMidLineWidth(0)
        self.semesterTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.semesterTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.semesterTable.setDragEnabled(True)
        self.semesterTable.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.semesterTable.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.semesterTable.setRowCount(7)
        self.semesterTable.setColumnCount(2)
        self.semesterTable.setObjectName("semesterTable")

        # Set the horizontal header items for each semester
        item = QtWidgets.QTableWidgetItem()
        self.semesterTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.semesterTable.setHorizontalHeaderItem(1, item)

        # Adjust column widths for readability
        self.semesterTable.setColumnWidth(0, 200)  # Width for the first semester
        self.semesterTable.setColumnWidth(1, 200)  # Width for the second semester
        
        # Enable automatic resizing to fit content
        self.semesterTable.horizontalHeader().setStretchLastSection(True)
        self.semesterTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Set the text for the header items
        _translate = QtCore.QCoreApplication.translate
        item = self.semesterTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "1er Semestre"))
        item = self.semesterTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "2do Semestre"))
    
    def handle_main_menu(self):
        pass  # Already on the Main Menu screen

    def handle_profile(self):
        self.view_profile.emit()

    def handle_courses(self):
        self.view_courses.emit()

    def confirm_logout(self):
        reply = QMessageBox.question(self, 'Log Out',
                                     "Are you sure you want to log out?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.logout.emit()
    
    def add_course_to_list(self, course: Course_Eligibility.CourseEligibility, status):
        item = QtWidgets.QListWidgetItem(course.code)  # Only display the course code

        # Set the tooltip with additional course details
        tooltip = (
            f"Course Name: {course.name}\n"
            f"Credits: {course.credits}\n"
            f"Suggested Semester: {course.suggested_semester}"
        )
        item.setToolTip(tooltip)  # Set the tooltip for hover information

        # Set font and background color based on status
        font = QtGui.QFont()
        font.setBold(False)
        item.setFont(font)

        if status == "not taken":
            item.setBackground(QColor("#4CAF50"))  # Green for available courses
        elif status == "taken":
            item.setBackground(QColor("#03b6fc"))  # Blue for passed courses
        elif status == "cant take":
            item.setBackground(QColor("#FF0000"))  # Red for failed courses

        self.availCourselist.addItem(item)

    def populate_not_taken_courses(self, student_id):
        conn = db_connection.create_connection()
        if conn is None:
            QMessageBox.critical(self, "Database Error", "Failed to connect to the database.")
            return

        cursor = conn.cursor()
        try:
            courses = Course_Eligibility.get_not_taken_courses(student_id, conn, cursor)
            # self.availCourselist.clear()
            for course in courses:
                self.add_course_to_list(course, "not taken")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to fetch not-taken courses: {e}")
        finally:
            cursor.close()
            conn.close()

    def populate_taken_courses(self, student_id):
        conn = db_connection.create_connection()
        if conn is None:
            QMessageBox.critical(self, "Database Error", "Failed to connect to the database.")
            return

        cursor = conn.cursor()
        try:
            courses = Course_Eligibility.get_taken_courses(student_id, conn, cursor)
            for course in courses:
                self.add_course_to_list(course, "taken")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to fetch taken courses: {e}")
        finally:
            cursor.close()
            conn.close()
    
    def populate_courses_in_semester(self, table, semester_name):
        """
        Populates the given table with courses for the specified semester.
        """
        cursor = self.conn.cursor()
        try:
            # Fetch the planning_id for the semester
            query_planning = """
            SELECT planning_id FROM semester_planning
            WHERE student_id = %s AND semester_name = %s
            """
            cursor.execute(query_planning, (self.student_id, semester_name))
            result = cursor.fetchone()

            if not result:
                # No planning ID exists for the semester; no courses to populate
                return

            planning_id = result[0]

            # Fetch courses associated with the planning_id
            query_courses = """
            SELECT pc.course_code, c.course_name, c.credits
            FROM planned_courses pc
            JOIN courses c ON pc.course_code = c.course_code
            WHERE pc.planning_id = %s
            """
            cursor.execute(query_courses, (planning_id,))
            courses = cursor.fetchall()

            # Populate the table with the fetched courses
            for course_code, course_name, credits in courses:
                row = table.rowCount()
                table.insertRow(row)
                table.setItem(row, 0, QTableWidgetItem(course_code))
                table.setItem(row, 1, QTableWidgetItem(f"{course_name} ({credits} credits)"))

        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Failed to fetch courses for semester {semester_name}: {e}")
        finally:
            cursor.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())
