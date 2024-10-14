import tkinter as tk
root = tk.Tk()
root.title("hello tkinter")
label = tk.Label(root ,  text="welcome here!")
label.pack()
button = tk.Button(root , text="click me", command=root.quit)
root.mainloop()