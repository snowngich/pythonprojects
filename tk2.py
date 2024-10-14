import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello Tkinter")

# Create a label widget
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me", command=root.quit)
button.pack()

# Run the application
root.mainloop()
