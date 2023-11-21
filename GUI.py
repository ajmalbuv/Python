import tkinter as tk
# create the main window
root = tk.Tk()
root.title("My first page")
root.geometry("400x400")
# create a label
label = tk.Label(root, text="Welcome to Computer lab",
                 font=("TkDefaultFont", 20))
label.pack()
# start the GUI event loop
root.mainloop()
