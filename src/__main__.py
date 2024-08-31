import tkinter as tk

# ---
# NOTE: *incompleted
# Eventually the labels on the stdin, stdout, stderr from the module "client.py"
# would be imported here in a way that the user could type cmd inputs and client.py 
# will read them.
# ---

def main():
    # main window
    root = tk.Tk()
    
    # label widget example
    label = tk.Label(root, text='testing')
    label.pack()
    
    # This updates the GUI event at a certain framerate
    root.mainloop()

if __name__ == "__main__":
    main()