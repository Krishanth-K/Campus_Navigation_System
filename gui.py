import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

#main window
root = tk.Tk()
root.title("CNS")
root.geometry("1200x600")

#custom font
cusfont=tkfont.Font(family="Aptos",size=12)

#2 grids- left and right
left = tk.Frame(root, width=300, height=600, bg="black")
left.grid(row=0, column=0, sticky="nswe")

right = tk.Frame(root, width=900, height=600, bg="white")
right.grid(row=0, column=1, sticky="nswe")  # Correctly place the right frame

#grid configuration
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

#dropdown menu
selection = tk.Label(left, text="Select destination", fg="white", bg="black",font=cusfont)
selection.place(relx=0.5, rely=0.4, anchor="center")  

#menu
options = ["AB1", "AB2", "AB3", "AB4", "Library", "Main Canteen", "IT Canteen", "Business Canteen", "Business School", "Playground"]
sel = tk.StringVar()
menu = ttk.Combobox(left, values=options, textvariable=sel,font=cusfont)
menu.place(relx=0.5, rely=0.5, anchor="center")  

#button function
def butclick():
    selopt=sel.get()
    result.config(text=f"Selected Destination: {selopt}",font=cusfont)

#result label
result=tk.Label(left,text="",fg="white",bg="black")
result.place(relx=0.5,rely=0.7,anchor="center")

#button
button=tk.Button(left,text="Confirm selection",command=butclick)
button.place(relx=0.5,rely=0.6,anchor="center")

root.mainloop()
