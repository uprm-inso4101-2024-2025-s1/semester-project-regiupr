import tkinter as tk
from tkinter import font, messagebox
from tkinter import PhotoImage
from courses import search_courses
from language import selected_language
import os

# List to store enrolled classes
enrolled_classes = []

# Dictionary with the vocabulary which it is going to apper in the interface
current_language = 'spanish'
text = selected_language(current_language)

def display_results(results):
    """
    Displays the search results in a grid of cards, each representing a course.
    Clears previous results before displaying new ones.
    """
    # Clear previous results
    for widget in result_frame_inner.winfo_children():
        widget.destroy()

    num_columns = 2  # Number of columns for displaying course cards
    card_width = 500  # Width of each course card

    # Calculate number of rows needed
    num_rows = (len(results) + num_columns - 1) // num_columns

    for idx, course in enumerate(results):
        # Create a string of section codes for the course
        sections_str = ", ".join([section['section_code'] for section in course['sections']])

        # Create a frame for each course card
        card_frame = tk.Frame(result_frame_inner, bg="#ffffff", borderwidth=1, relief="solid", padx=10, pady=10, width=card_width)
        card_frame.grid(row=idx // num_columns, column=idx % num_columns, padx=5, pady=5, sticky="nsew")

        content_frame = tk.Frame(card_frame, bg="#ffffff")
        content_frame.pack(fill=tk.BOTH, expand=True)

        # Label for course code and name
        course_label = tk.Label(content_frame, text=f"{course['code']} - {course['name']}", font=("Helvetica", 12, "bold"))
        course_label.pack(anchor=tk.W)

        # Label for sections
        sections_label = tk.Label(content_frame, text=f"{text["display_results"][0]} {sections_str}", font=("Helvetica", 10))
        sections_label.pack(anchor=tk.W)

        # Label for department
        department_label = tk.Label(content_frame, text=f"{text["display_results"][1]} {course['department']}", font=("Helvetica", 10, "bold"), bg="#ffffff")
        department_label.pack(anchor=tk.W, pady=5)

        button_frame = tk.Frame(card_frame, bg="#ffffff")
        button_frame.pack(fill=tk.X, pady=(5, 0))

        # Button for showing more details
        details_button = tk.Button(button_frame, text=text["display_results"][2], command=lambda c=course: show_details(c))
        details_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Button for enrolling in the course
        enroll_button = tk.Button(button_frame, text=text["display_results"][3], command=lambda c=course: show_sections(c))
        enroll_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Configure grid weights to resize columns and rows proportionally
    for i in range(num_columns):
        result_frame_inner.columnconfigure(i, weight=1)
    result_frame_inner.rowconfigure(list(range(num_rows)), weight=1)

    # Update scroll region of the canvas
    result_canvas.configure(scrollregion=result_canvas.bbox("all"))

def show_details(course):
    """
    Displays details for a selected course.
    """
    print(f"Details for {course['code']} - {course['name']}")

def show_sections(course):
    """
    Opens a new window to display sections for a selected course and allows enrollment.
    """
    section_window = tk.Toplevel(root)
    section_window.title(f"{text["show_sections"][0]} {course['code']}")

    section_canvas = tk.Canvas(section_window, bg="#f0f0f0")
    section_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(section_window, orient=tk.VERTICAL, command=section_canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    section_canvas.config(yscrollcommand=scrollbar.set)

    section_frame = tk.Frame(section_canvas, bg="#f0f0f0")
    section_canvas.create_window((0, 0), window=section_frame, anchor=tk.NW)

    section_frame.bind("<Configure>", lambda e: section_canvas.configure(scrollregion=section_canvas.bbox("all")))

    num_columns = 2  # Number of columns for displaying section cards
    card_width = 400  # Width of each section card

    for idx, section in enumerate(course['sections']):
        # Create a frame for each section card
        card_frame = tk.Frame(section_frame, bg="#ffffff", borderwidth=1, relief="solid", padx=10, pady=10, width=card_width)
        card_frame.grid(row=idx // num_columns, column=idx % num_columns, padx=5, pady=5, sticky="nsew")

        # Label for section code
        section_label = tk.Label(card_frame, text=f"{text["show_sections"][1]} {section['section_code']}", font=("Helvetica", 12, "bold"))
        section_label.pack(anchor=tk.W)

        # Label for class days
        days_label = tk.Label(card_frame, text=f"{text["show_sections"][2]} {section['days']}", font=("Helvetica", 10))
        days_label.pack(anchor=tk.W)

        # Label for class hours
        hours_label = tk.Label(card_frame, text=f"{text["show_sections"][3]} {section['hours']}", font=("Helvetica", 10))
        hours_label.pack(anchor=tk.W)

        # Label for availability
        available_text = text["show_sections"][4] if section['available'] else text["show_sections"][5]
        availability_label = tk.Label(card_frame, text=f"{text["show_sections"][6]} {available_text}", font=("Helvetica", 10, "bold" if section['available'] else "normal"))
        availability_label.pack(anchor=tk.W)

        # Button to enroll in the section
        enroll_button = tk.Button(card_frame, text=text["show_sections"][7], state="normal" if section['available'] else "disabled",
                                  command=lambda s=section: enroll_section(s, course, section_window))
        enroll_button.pack(pady=5)

    # Configure grid weights to resize columns and rows proportionally
    for i in range(num_columns):
        section_frame.columnconfigure(i, weight=1)
    section_frame.rowconfigure(list(range((len(course['sections']) + num_columns - 1) // num_columns)), weight=1)

    # Bind mouse wheel scrolling to canvas
    section_window.bind_all("<MouseWheel>", lambda event: section_canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

def enroll_section(section, course, section_window):
    """
    Enrolls in the selected section if available and updates the list of enrolled classes.
    """
    if section['available']:
        response = messagebox.askyesno(text["enroll_section"][0], f"{text["enroll_section"][1]} {section['section_code']} {text["enroll_section"][2]} {course['code']}?")
        if response:
            enrolled_classes.append({
                "course_code": course['code'],
                "course_name": course['name'],
                "section_code": section['section_code'],
                "class_days": section['days'],
                "class_hours": section['hours']
            })
            messagebox.showinfo(text["enroll_section"][4], f"{text["enroll_section"][5]} {section['section_code']} {text["enroll_section"][6]} {course['code']}.")
            section_window.destroy()
    else:
        messagebox.showwarning(text["enroll_section"][4], f"{text["show_sections"][8]} {section['section_code']} {text["show_sections"][9]}")

def show_enrolled_courses():
    """
    Opens a new window displaying all enrolled courses in a table format.
    """
    enrolled_window = tk.Toplevel(root)
    enrolled_window.title(text["show_enrolled_courses"][0])

    table_frame = tk.Frame(enrolled_window, padx=10, pady=10)
    table_frame.pack(fill=tk.BOTH, expand=True)

    headers = text["headers"]
    # Create header labels
    for col, header in enumerate(headers):
        header_label = tk.Label(table_frame, text=header, font=("Helvetica", 12, "bold"), borderwidth=1, relief="solid")
        header_label.grid(row=0, column=col, sticky="nsew")

    # Create labels for enrolled courses
    for row, course in enumerate(enrolled_classes, start=1):
        values = [course["course_code"], course["course_name"], course["section_code"], course["class_days"], course["class_hours"]]
        for col, value in enumerate(values):
            cell_label = tk.Label(table_frame, text=value, font=("Helvetica", 10), borderwidth=1, relief="solid")
            cell_label.grid(row=row, column=col, sticky="nsew")

    # Configure grid weights to resize columns and rows proportionally
    for col in range(len(headers)):
        table_frame.grid_columnconfigure(col, weight=1)
    table_frame.grid_rowconfigure(list(range(len(enrolled_classes) + 1)), weight=1)

def toggle_side_panel():
    """
    Toggles the visibility of the side panel that contains menu options.
    """
    global side_panel_visible
    if side_panel_visible:
        side_panel.pack_forget()
        side_panel_visible = False
    else:
        side_panel.pack(side=tk.RIGHT, fill=tk.BOTH)
        side_panel_visible = True

def change_language():
    if current_language == 'spanish':
        text = selected_language('english')
        current_language == 'english'
    else:
        text = selected_language('spanish')
        current_language == 'spanish'

def on_search(*args):
    """
    Handles search input changes, performs a search, and displays results.
    """
    query = search_var.get().strip().lower()
    if query:
        results = search_courses(query)
        if results:
            display_results(results)
            error_label.pack_forget()
        else:
            error_label.config(text=text["on_search"][0])
            error_label.pack()
            display_results([])
    else:
        display_results([])

def on_mouse_wheel(event):
    """
    Handles mouse wheel scrolling for the result canvas.
    """
    result_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Create the main application window
root = tk.Tk()
root.title("RegiUPR © Software")

# Define custom font for labels and buttons
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Load the logo image
logo_path = os.path.join(os.path.dirname(__file__), 'resources', 'RegiUPR.png')
logo = PhotoImage(file=logo_path)
logo = logo.subsample(10, 10)

# Create the banner frame and add logo and title
banner_frame = tk.Frame(root, bg="#4CAF50", height=100)
banner_frame.pack(fill=tk.X)

logo_title_frame = tk.Frame(banner_frame, bg="#4CAF50")
logo_title_frame.pack(pady=10)

logo_label = tk.Label(logo_title_frame, image=logo, bg="#4CAF50")
logo_label.pack(side=tk.LEFT, padx=10)

title_label = tk.Label(logo_title_frame, text=text["other"][0], bg="#4CAF50", fg="white", font=("Helvetica", 16, "bold"))
title_label.pack(side=tk.LEFT, padx=450)

# Menu button setup
menu_button = tk.Button(logo_title_frame, text="☰", font=("Helvetica", 20), bg="#4CAF50", fg="white", borderwidth=0, command=toggle_side_panel)
menu_button.pack(side=tk.RIGHT, padx=10)

# Menu button setup
lang_button = tk.Button(logo_title_frame, text="LANG", font=("Helvetica", 20), bg="#4CAF50", fg="white", borderwidth=0, command=change_language)
lang_button.pack(side=tk.RIGHT, padx=10)

# Create search frame and search bar
search_frame = tk.Frame(root, padx=10, pady=10)
search_frame.pack(fill=tk.X)

title_label = tk.Label(search_frame, text=text["other"][1], font=("Helvetica", 12))
title_label.pack(side=tk.TOP, anchor=tk.CENTER)

search_var = tk.StringVar()
search_var.trace_add("write", on_search)

search_entry = tk.Entry(search_frame, textvariable=search_var, font=("Helvetica", 14), width=40)
search_entry.pack(side=tk.TOP, padx=10)

# Create result frame with canvas for displaying search results
result_frame = tk.Frame(root)
result_frame.pack(fill=tk.BOTH, expand=True)

result_canvas = tk.Canvas(result_frame)
result_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(result_frame, orient=tk.VERTICAL, command=result_canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_canvas.config(yscrollcommand=scrollbar.set)

result_frame_inner = tk.Frame(result_canvas)
result_canvas.create_window((0, 0), window=result_frame_inner, anchor=tk.NW)

result_frame_inner.bind("<Configure>", lambda e: result_canvas.configure(scrollregion=result_canvas.bbox("all")))
root.bind_all("<MouseWheel>", on_mouse_wheel)

# Label for displaying errors
error_label = tk.Label(search_frame, text="", fg="red", font=("Helvetica", 12, "bold"))
error_label.pack(side=tk.TOP, pady=100)

# Create side panel for menu options
side_panel = tk.Frame(result_canvas, bg="#4CAF50", width=200)
side_panel_visible = False

# Button to show enrolled courses
enrolled_courses_button = tk.Button(side_panel, text=text["other"][2], font=("Helvetica", 12), bg="#4CAF50", fg="white", command=show_enrolled_courses)
enrolled_courses_button.pack(padx=10, pady=10, fill=tk.X)

# Start the Tkinter event loop
root.mainloop()
