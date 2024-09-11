# Main_Menu.py
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QSizePolicy
from PyQt5.QtCore import Qt, QTime
from PyQt5.QtGui import QFont, QBrush, QColor

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize the main window
        self.setup_window()
        
        # Set up the central layout and components
        self.setup_main_layout()

    def setup_window(self):
        """Set up the main window properties."""
        self.setWindowTitle("RegiUPR")
        self.setGeometry(100, 100, 1024, 768)
    
    def setup_main_layout(self):
        """Configure the main layout including the side panel and content area."""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout (horizontal) with side panel and content area
        main_layout = QHBoxLayout(central_widget)
        
        # Create the side panel and content layout
        self.create_side_menu(main_layout)
        self.create_content_layout(main_layout)
        
    def create_side_menu(self, layout):
        """Creates the side menu with navigation buttons."""
        side_menu = QWidget(self)
        side_menu.setFixedWidth(200)
        side_menu.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        side_menu.setStyleSheet("background-color: green;")
        
        # Layout for the side menu
        side_menu_layout = QVBoxLayout(side_menu)
        
        # Side menu buttons
        buttons = ["Main Menu", "Profile", "Logout"]
        for button in buttons:
            self.add_side_menu_button(side_menu_layout, button)
        
        side_menu_layout.addStretch()  # Pushes buttons to the top
        layout.addWidget(side_menu)

    def add_side_menu_button(self, layout, text):
        """Helper function to add buttons to the side menu."""
        btn = QPushButton(text, self)
        btn.setFont(QFont("Helvetica", 14))
        btn.setStyleSheet("background-color: white; color: black;")
        layout.addWidget(btn)

    def create_content_layout(self, layout):
        """Create the main content area with labels and tables."""
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        layout.addWidget(content_widget)
        
        # Add welcome and enrollment labels
        self.add_header_label(content_layout, "Welcome, User!", 24)
        self.add_header_label(content_layout, "Enrollment Schedule", 18)

        # Add schedule table
        self.schedule_table = self.create_schedule_table()
        content_layout.addWidget(self.schedule_table)
        
        # Add courses in enrollment label and table
        self.add_header_label(content_layout, "Courses In Enrollment", 18)
        self.enrollment_table = self.create_enrollment_table()
        content_layout.addWidget(self.enrollment_table)

    def add_header_label(self, layout, text, font_size):
        """Helper function to add a header label."""
        label = QLabel(text, self)
        label.setFont(QFont("Helvetica", font_size, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

    def create_schedule_table(self):
        """Creates the table for displaying the class schedule."""
        schedule_table = QTableWidget(self)
        schedule_table.setRowCount(30)  # 30-minute intervals
        schedule_table.setColumnCount(6)  # Time + 5 days
        schedule_table.setHorizontalHeaderLabels(["Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
        schedule_table.verticalHeader().setVisible(False)  # Hide row labels
        schedule_table.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: lightgrey; border: 1px solid black; }")
        schedule_table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        # Set up time frames in the first column
        self.populate_time_column(schedule_table)

        # Add sample schedule data
        self.populate_schedule_data(schedule_table)

        # Set black outline for the table
        schedule_table.setStyleSheet("""
            QTableWidget {
                gridline-color: black;
                border: 1px solid black;
            }
            QTableWidget::item {
                border: 1px solid black;
            }
        """)
        schedule_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        schedule_table.setColumnWidth(0, 100)

        return schedule_table

    def populate_time_column(self, table):
        """Populates the first column of the schedule table with time frames."""
        time_frames = [
            "6:30 AM", "7:00 AM", "7:30 AM", "8:00 AM", "8:30 AM", 
            "9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", 
            "11:30 AM", "12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM", 
            "2:00 PM", "2:30 PM", "3:00 PM", "3:30 PM", "4:00 PM", 
            "4:30 PM", "5:00 PM", "5:30 PM", "6:00 PM", "6:30 PM", 
            "7:00 PM", "7:30 PM", "8:00 PM", "8:30 PM", "9:00 PM"
        ]

        for i, time in enumerate(time_frames):
            item = QTableWidgetItem(time)
            item.setTextAlignment(Qt.AlignCenter)
            table.setItem(i, 0, item)

    def populate_schedule_data(self, table):
        """Fills in the schedule table with sample class blocks."""
        schedule_data = [
            ("8:30 AM", "9:20 AM", "Monday", "MATE4009-030\nSalon: M-315", QColor(176, 196, 222)),
            ("10:30 AM", "11:20 AM", "Tuesday", "INEL3105-040\nSalon: S-227", QColor(144, 238, 144)),
            ("1:30 PM", "3:00 PM", "Thursday", "ICOM4009-080\nSalon: S-113", QColor(255, 182, 193)),
        ]

        for start_time, end_time, day, course_info, color in schedule_data:
            start_row = self.time_to_row(start_time)
            end_row = self.time_to_row(end_time)
            if start_row == -1 or end_row == -1:
                continue  # Skip invalid times
            day_column = self.day_to_column(day)
            self.fill_table_block(table, start_row, end_row, day_column, course_info, color)

    def time_to_row(self, time):
        """Converts time string to the corresponding row index."""
        time_obj = QTime.fromString(time, "h:mm AP")
        if time_obj.isValid():
            return (time_obj.hour() - 6) * 2 + (1 if time_obj.minute() == 30 else 0)
        return -1

    def day_to_column(self, day):
        """Maps day string to the corresponding column index."""
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days.index(day) + 1

    def fill_table_block(self, table, start_row, end_row, day_column, course_info, color):
        """Fills a block of rows in the table with course information."""
        for row in range(start_row, end_row + 1):
            item = QTableWidgetItem(course_info if row == start_row else "")
            item.setTextAlignment(Qt.AlignCenter)
            item.setBackground(QBrush(color))
            table.setItem(row, day_column, item)

    def create_enrollment_table(self):
        """Creates a table for displaying enrolled courses."""
        enrollment_table = QTableWidget(self)
        enrollment_table.setRowCount(5)  # Example row count
        enrollment_table.setColumnCount(5)  # Columns for course details
        enrollment_table.setHorizontalHeaderLabels(["Curso", "Sección", "Creditos", "Reuniones", "Profesores"])

        # Example data (this would be dynamic in a real app)
        courses = [
            ("INEL3105", "040", "3", "10:30 am - 11:20 am", "Jose M Rosado Roman"),
            ("INEL4205", "036", "3", "9:00 am - 10:15 am", "Hamed Parsiani Gobadi"),
            ("MATE4009", "030", "3", "9:30 am - 10:20 am", "Karen Rios Soto"),
            ("INGE3045", "086", "3", "2:00 pm - 3:15 pm", "Agnes Padovani Blanco"),
        ]
        
        for i, course in enumerate(courses):
            for j, info in enumerate(course):
                item = QTableWidgetItem(info)
                item.setTextAlignment(Qt.AlignCenter)
                enrollment_table.setItem(i, j, item)

        # Style the table
        enrollment_table.setStyleSheet("""
            QTableWidget {
                gridline-color: black;
                border: 1px solid black;
            }
            QTableWidget::item {
                border: 1px solid black;
            }
        """)
        enrollment_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        return enrollment_table
