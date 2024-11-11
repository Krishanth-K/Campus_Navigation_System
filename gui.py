import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

#main window
root = tk.Tk()
root.title("CNS")
root.geometry("1200x600")
root.state('zoomed')

#custom font
cusfont = tkfont.Font(family="Aptos", size=14)

#container frame
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True)

#main grid configuration
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

#left frame in main frame
left = tk.Frame(main_frame, width=300, height=600, bg="black")
left.grid(row=0, column=0, sticky="nswe")

#right frame in main frame
right = tk.Frame(main_frame, width=900, height=600, bg="white")
right.grid(row=0, column=1, sticky="nswe")


# Dropdown menu
def dropdown():
    global ask, sel, menu, confirmbutton, placeholder
    ask = ttk.Label(left, text="Select destination", font=cusfont, background="black", foreground="white")
    ask.place(relx=0.5, rely=0.3, anchor="center")
    
    # Dropdown menu options
    options = ["AB1", "AB2", "AB3", "AB4", "Library", "Main Canteen", "IT Canteen", "Business Canteen", "Business School", "Playground"]
    sel = tk.StringVar()

    # Create the Combobox
    menu = ttk.Combobox(left, values=options, textvariable=sel, font=cusfont)
    menu.place(relx=0.5, rely=0.5, anchor="center")

    # Add placeholder label centered on top of the dropdown
    placeholder = ttk.Label(left, text="Pick an option below", font=cusfont, foreground="gray")
    placeholder.place(relx=0.5, rely=0.5, anchor="center")

    # Hide the placeholder text when an option is selected
    def on_select(event):
        placeholder.place_forget()
    
    menu.bind("<<ComboboxSelected>>", on_select)

    # Confirm button
    confirmbutton = ttk.Button(left, text="Confirm selection", command=clconfirmbutton)
    confirmbutton.place(relx=0.5, rely=0.6, anchor="center")




#creating home button
def crhomebutton():
    global backbutton
    backbutton = ttk.Button(left, text="Home", command=clbackbutton)
    backbutton.place(relx=0.5, rely=0.9, anchor="center")

#clicking home button
def clbackbutton():
    resetui()
    dropdown()
    crhistorrybutton()
    backbutton.destroy()

#creating history button
def crhistorrybutton():
    global historybutton  
    historybutton = ttk.Button(left, text="View history", command=clhistorybutton)
    historybutton.place(relx=0.5, rely=0.7, anchor="center")

#clicking history button
def clhistorybutton():
    global log
    resetui()
    placeholder.destroy()
    try:
        disp.destroy()
    except:
        pass

    with open("cps.txt", "r") as file:
        history = file.read().strip()
    
    if not history:
        history = "No results"
    
    log = ttk.Label(left, text=history, font=cusfont, background="black", foreground="white")
    log.place(relx=0.5, rely=0.5, anchor="center")

    crclrhistorybutton()
    crhomebutton()


#creating clear history button
def crclrhistorybutton():
    global clrhistorybutton  
    clrhistorybutton = ttk.Button(left, text="Clear history", command=clclrhistorybutton)
    clrhistorybutton.place(relx=0.5, rely=0.7, anchor="center")

# clicking clear history button
def clclrhistorybutton():
    global clearmsg
    with open("cps.txt", "w") as file:
        pass
    log.destroy()
    clrhistorybutton.destroy()
    clearmsg = ttk.Label(left, text="History cleared", font=cusfont, background="black", foreground="white")
    clearmsg.place(relx=0.5, rely=0.5, anchor="center")


# clicking confirm button
def clconfirmbutton():
    global sel, ask, menu, confirmbutton, disp
    selopt = sel.get()

    if not selopt:
        disp = ttk.Label(left, text="No option selected", font=cusfont, background="black", foreground="white")
        placeholder.destroy()
    else:
        disp = ttk.Label(left, text=f"Selected Destination: {selopt}", font=cusfont, background="black", foreground="white")
        with open("cps.txt", "a") as file:
            file.write(f"{selopt}\n")

    disp.place(relx=0.5, rely=0.4, anchor="center")
    ask.destroy()
    menu.destroy()
    confirmbutton.destroy()
    placeholder.destroy()

    crhomebutton()
    crhistorrybutton()


#reset user interface
def resetui():
    try:
        ask.destroy()
        menu.destroy()
        confirmbutton.destroy()
        historybutton.destroy()
        backbutton.destroy()
        disp.destroy()
        log.destroy()
        clrhistorybutton.destroy()
        clearmsg.destroy()
    except:
        pass

def start():
    dropdown()
    crhomebutton()
    crhistorrybutton()


start()

root.mainloop()
