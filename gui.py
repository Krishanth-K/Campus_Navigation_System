import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

# main window
root = tk.Tk()
root.title("CNS")
root.geometry("1200x600")
root.state('zoomed')

# custom font
cusfont = tkfont.Font(family="Helvetica", size=14)

# container frame
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True)

# grid configuration for the main frame
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

# left and right frames inside main_frame
left = tk.Frame(main_frame, width=300, height=600, bg="black")
left.grid(row=0, column=0, sticky="nswe")

right = tk.Frame(main_frame, width=900, height=600, bg="white")
right.grid(row=0, column=1, sticky="nswe")

# dropdown menu in left frame
selection = ttk.Label(left, text="Select destination", font=cusfont, background="black", foreground="white")
selection.place(relx=0.5, rely=0.4, anchor="center")

# menu
options = ["AB1", "AB2", "AB3", "AB4", "Library", "Main Canteen", "IT Canteen", "Business Canteen", "Business School", "Playground"]
sel = tk.StringVar()
menu = ttk.Combobox(left, values=options, textvariable=sel, font=cusfont)
menu.place(relx=0.5, rely=0.5, anchor="center")

# button function
def butclick():
    selopt = sel.get()
    result.config(text=f"Selected Destination: {selopt}")

# result label
result = ttk.Label(left, text="", font=cusfont, background="black", foreground="white")
result.place(relx=0.5, rely=0.7, anchor="center")

# button
button = ttk.Button(left, text="Confirm selection", command=butclick)
button.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()
