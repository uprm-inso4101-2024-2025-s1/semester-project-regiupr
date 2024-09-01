
# RegiUPR Course Enrollment System

<img src="https://github.com/user-attachments/assets/eddd6ae2-f88a-4e35-a911-515546fde101" alt="Description of Image" width="300"/>

## Overview

The **RegiUPR Course Enrollment System** is a Tkinter-based desktop application designed to streamline the course enrollment process for students. The system allows students to search for courses by course code, view course details, enroll in sections, and manage their enrolled courses. The application also includes a side panel with easy navigation options for accessing enrolled courses and other features.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [License](#license)
- [Acknowledgments](#acknowledgments)


## Features

- **Course Search**: Search for courses by course code and view available sections.
- **Enrollment**: Enroll in specific sections of courses, with real-time availability checks.
- **Enrolled Courses Management**: View a table of all enrolled courses with detailed information for each course such as Course Code, Course Name, Enrolled Section, and more.
- **Multi-Language Support**: Supports English and Spanish (at the moment) to make enrollment easier for all types of students.

## Installation

### Prerequisites
- Python (3.x and newer)
- Tkinter (usually included with Python)
- PyInstaller (if you want to create an executable)

To set up the RegiUPR Course Enrollment System on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/regiupr-course-enrollment.git
   cd regiupr-course-enrollment
   ```
   
2. **Install dependencies**:

   Ensure you have Python 3.x or newer installed on your system. Install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Run the application**:
   ```bash
   python main.py
   ```
   
4. **Create an executable (optional)**:

   To create an executable using PyInstaller:
   ```bash
   pyinstaller --onefile --windowed main.py
   ```
   This will generate an executable file in the dist directory.

## Usage

1. **Start the application**: Run the '**main.py**' file.
   
2. **Search for a course**: Type the course code (e.g., '**ICOM4009**') in the search bar. Matching results will appear as you type.
   
3. **View course details**: Click on "**More Details**" to view additional information about a course.
   
4. **Enroll in a course**: Click "**Enroll**" to view available sections and enroll in one if it's available.
   
5. **View enrolled courses**: Access the list of enrolled courses via the side panel menu.

## File Structure

```bash
  RegiUPR/
│
├── courses.py          # Contains course-related functions and data
├── main.py             # Main entry point for the application
├── resources/          # Directory for images and other resources
│   └── RegiUPR.png     # Logo image
├── README.md           # Project documentation
├── requirements.txt    # List of dependencies
└── .gitignore          # Git ignore file
```

## Dependencies 

- **Python** (3.x and newer)
- **Tkinter**: Python's de-facto standard GUI package.
- **PyInstaller**: A package to bundle the application into a standalone executable (optional).

To install these dependencies, use the following command:

```bash
 pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Acknowledgements

- **[University of Puerto Rico](https://www.upr.edu/)** - For providing the environment and resources to develop this project.
- **[Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)** - For the comprehensive documentation on Tkinter used in this application.
- **[PyInstaller Documentation](https://pyinstaller.org/)** - For guidance on creating executable files from Python scripts.
- **[Stack Overflow](https://stackoverflow.com/)** - For community support and solutions to various coding issues encountered during development.
- **[GitHub](https://github.com/)** - For version control and collaboration features.
