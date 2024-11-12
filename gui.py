import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

# Main window
root = tk.Tk()
root.title("CNS")
root.geometry("1200x600")
root.state('zoomed')

# Custom font
cusfont = tkfont.Font(family="Aptos", size=14)

# Container frame
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Main grid configuration
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

# Left frame in main frame
left = tk.Frame(main_frame, width=300, height=600, bg="black")
left.grid(row=0, column=0, sticky="nswe")

# Right frame in main frame
right = tk.Frame(main_frame, width=900, height=600, bg="white")
right.grid(row=0, column=1, sticky="nswe")

<<<<<<< HEAD
# Dropdown menu
def dropdown():
    global ask, sel, menu, confirmbutton, placeholder
    global ask0, sel0, menu0, placeholder0
    
    #starting point menu
    options = ["Main gate","AB1", "AB2", "AB3", "Library", "Canteen", "Main office", "Post Office"]
    sel = tk.StringVar()
    sel0 = tk.StringVar()
    
    ask0 = ttk.Label(left, text="Select Starting point", font=cusfont, background="black", foreground="white")
    ask0.place(relx=0.5, rely=0.2, anchor="center")
    menu0 = ttk.Combobox(left, values=options, textvariable=sel0, font=cusfont,state="readonly")
    menu0.place(relx=0.5, rely=0.3, anchor="center")
    placeholder0 = ttk.Label(left, text="Pick an option below", font=cusfont, foreground="gray")
    placeholder0.place(relx=0.5, rely=0.3, anchor="center")

    def on_select0(event):
        placeholder0.place_forget()
    menu0.bind("<<ComboboxSelected>>", on_select0)
    
    #destination menu
    ask = ttk.Label(left, text="Select destination", font=cusfont, background="black", foreground="white")
    ask.place(relx=0.5, rely=0.4, anchor="center")
    menu = ttk.Combobox(left, values=options, textvariable=sel, font=cusfont,state="readonly")
    menu.place(relx=0.5, rely=0.5, anchor="center")
    placeholder = ttk.Label(left, text="Pick an option below", font=cusfont, foreground="gray")
    placeholder.place(relx=0.5, rely=0.5, anchor="center")
    
    def on_select(event):
        placeholder.place_forget()
    menu.bind("<<ComboboxSelected>>", on_select)
=======
>>>>>>> 776992963b985d428d91c1ca50cb9cba5964a128

# Dropdown menu
def dropdown():
    global ask, sel, menu, confirmbutton, placeholder
    global ask0, sel0, menu0, placeholder0
    
    ask = ttk.Label(left, text="Select destination", font=cusfont, background="black", foreground="white")
    ask.place(relx=0.5, rely=0.4, anchor="center")

    # Dropdown menu options
    options = ["AB1", "AB2", "AB3", "AB4", "Library", "Main Canteen", "IT Canteen", "Business Canteen", "Business School", "Playground"]
    
    sel = tk.StringVar()
    sel0 = tk.StringVar()  # Separate variable for the second dropdown

    # Create the Combobox for destination
    menu = ttk.Combobox(left, values=options, textvariable=sel, font=cusfont,state="readonly")
    menu.place(relx=0.5, rely=0.5, anchor="center")
    
    # Placeholder label centered on top of the dropdown
    placeholder = ttk.Label(left, text="Pick an option below", font=cusfont, foreground="gray")
    placeholder.place(relx=0.5, rely=0.5, anchor="center")
    
    # Hide the placeholder text when an option is selected in the first dro"pdown
    def on_select(event):
        placeholder.place_forget()
    menu.bind("<<ComboboxSelected>>", on_select)

    # Create the second dropdown for starting point
    ask0 = ttk.Label(left, text="Select Starting point", font=cusfont, background="black", foreground="white")
    ask0.place(relx=0.5, rely=0.2, anchor="center")
    
    menu0 = ttk.Combobox(left, values=options, textvariable=sel0, font=cusfont,state="readonly")
    menu0.place(relx=0.5, rely=0.3, anchor="center")
    
    # Placeholder label for the second dropdown
    placeholder0 = ttk.Label(left, text="Pick an option below", font=cusfont, foreground="gray")
    placeholder0.place(relx=0.5, rely=0.3, anchor="center")

    # Hide the placeholder text when an option is selected in the second dropdown
    def on_select0(event):
        placeholder0.place_forget()
    menu0.bind("<<ComboboxSelected>>", on_select0)

    # Confirm button
    confirmbutton = ttk.Button(left, text="Confirm selection", command=clconfirmbutton)
    confirmbutton.place(relx=0.5, rely=0.6, anchor="center")

<<<<<<< HEAD
=======

>>>>>>> 776992963b985d428d91c1ca50cb9cba5964a128
# Creating home button
def crhomebutton():
    global backbutton
    backbutton = ttk.Button(left, text="Home", command=clbackbutton)
    backbutton.place(relx=0.5, rely=0.9, anchor="center")

<<<<<<< HEAD
=======

>>>>>>> 776992963b985d428d91c1ca50cb9cba5964a128
# Clicking home button
def clbackbutton():
    resetui()
    dropdown()
    crhistorrybutton()
    crhomebutton()

<<<<<<< HEAD
=======

>>>>>>> 776992963b985d428d91c1ca50cb9cba5964a128
# Creating history button
def crhistorrybutton():
    global historybutton  
    historybutton = ttk.Button(left, text="View history", command=clhistorybutton)
    historybutton.place(relx=0.5, rely=0.7, anchor="center")

<<<<<<< HEAD
=======

>>>>>>> 776992963b985d428d91c1ca50cb9cba5964a128
# Clicking history button
def clhistorybutton():
    global log
    resetui()
    try:
        with open("history.txt", "r") as file:
            history = file.read().strip() or "No results"
    except FileNotFoundError:
        history = "No results"
    
    log = ttk.Label(left, text=history, font=cusfont, background="black", foreground="white")
    log.place(relx=0.5, rely=0.5, anchor="center")

    crclrhistorybutton()
    crhomebutton()

<<<<<<< HEAD
=======

>>>>>>> 776992963b985d428d91c1ca50cb9cba5964a128
# Creating clear history button
def crclrhistorybutton():
    global clrhistorybutton  
    clrhistorybutton = ttk.Button(left, text="Clear history", command=clclrhistorybutton)
    clrhistorybutton.place(relx=0.5, rely=0.7, anchor="center")

<<<<<<< HEAD
# Clicking clear history button
def clclrhistorybutton():
=======

# Clicking clear history button
def clclrhistorybutton():
    global clearmsg
>>>>>>> 776992963b985d428d91c1ca50cb9cba5964a128
    with open("history.txt", "w") as file:
        pass
    log.config(text="History cleared")
    clrhistorybutton.destroy()

<<<<<<< HEAD
=======

>>>>>>> 776992963b985d428d91c1ca50cb9cba5964a128
# Clicking confirm button
def clconfirmbutton():
    selopt = sel.get()
    startopt = sel0.get()

    if not selopt:
        disp_text = "No option selected for destination"
    elif not startopt:
        disp_text = "No option selected for starting point"
    else:
        disp_text = f"Showing route From {startopt} to {selopt}"
        with open("history.txt", "a") as file:
            file.write(f"{startopt} -> {selopt}\n")

    resetui()
    global disp
    disp = ttk.Label(left, text=disp_text, font=cusfont, background="black", foreground="white")
    disp.place(relx=0.5, rely=0.4, anchor="center")

    crhomebutton()
    crhistorrybutton()

<<<<<<< HEAD
# Reset user interface
def resetui():
    for widget in left.winfo_children():
        widget.destroy()

#Start function
=======

# Reset user interface
def resetui():
    # Remove all widgets in the left frame to ensure placeholders and labels are cleared
    for widget in left.winfo_children():
        widget.destroy()


# Start function
>>>>>>> 776992963b985d428d91c1ca50cb9cba5964a128
def start():
    dropdown()
    crhomebutton()
    crhistorrybutton()
<<<<<<< HEAD
=======

>>>>>>> 776992963b985d428d91c1ca50cb9cba5964a128

start()

root.mainloop()
