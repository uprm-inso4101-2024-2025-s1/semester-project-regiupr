import tkinter as tk
from tkinter import messagebox

# Creating window and properties
root = tk.Tk()                  
root.title("Login to RegiUPR")
root.geometry("340x380")

# Method verifies user input with stored data.
# If succesful, the window will close and open the main screen.
# Additionally will have the option to sign up or 
# attempt to recover lost credentials.
# *
def login():
    username = "juan.delpueblo@upr.edu"
    studentID = "000000000"
    password = "ansiedad"

    if user_entry.get()==username and sid_entry.get()==studentID and pass_entry.get()==password:
        messagebox.showinfo(title="Welcome", message="Login Successful")
    else:
        messagebox.showerror(title="Error", message="Invalid Login")

#def signup():

#def recov():
    


frame = tk.Frame()

# Creating widgets
welc_label = tk.Label(frame, text="Welcome to RegiUPR", bg="#4CAF50", font=('Helvetica', 24, "bold"))
user_label = tk.Label(frame, text="Username", font=('Helvetica', 16))
user_entry = tk.Entry(frame)
sid_label = tk.Label(frame, text="Student ID", font=('Helvetica', 16))
sid_entry = tk.Entry(frame)
pass_label = tk.Label(frame, text="Password", font=('Helvetica', 16))
pass_entry = tk.Entry(frame, show="*")
login_button = tk.Button(frame, text="Login", bg='#4CAF50', command=login)
signup_button = tk.Button(frame, text="Sign Up", bg='#4CAF50')
cant_button = tk.Button(frame, text="Can't Login", bg='#4CAF50')

# Placing widgets on screen
welc_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
user_label.grid(row=1, column=0)
user_entry.grid(row=1, column=1, pady=10)
sid_label.grid(row=2, column=0)
sid_entry.grid(row=2, column=1, pady=10)
pass_label.grid(row=3, column=0)
pass_entry.grid(row=3, column=1, pady=10)
login_button.grid(row=4, column=0, columnspan=2, pady=5)
signup_button.grid(row=5, column=0, columnspan=2, pady=5)
cant_button.grid(row=6, column=0, columnspan=2, pady=5)

# Keeps window contents centered
frame.pack()

frame.mainloop()