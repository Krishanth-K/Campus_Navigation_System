import os
import heapq
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from parser import ParseFile
from math import sqrt


# markers are "location pins" on the map
class Marker():
    def __init__(self, coords, name=None, color="Red"):
        self.coords = coords
        self.name = name
        self.color = color


# subclass of Marker with default color as blue
class LocationMarker(Marker):
    def __init__(self, coords, name=None, color="blue"):
        super().__init__(coords, name, color)


# subclass of Marker with default color as green
class PathMarker(Marker):
    def __init__(self, coords, name=None, color="red"):
        super().__init__(coords, name, color)


def CloseWindow(event=None):
    root.destroy() 


# draws the markers on the canvas provided
def DrawMarkers(markers, canvas):

    # checks if the markers is list of markers or a single marker
    if isinstance(markers, list):

        for marker in markers:
            if isinstance(marker, list):

                for i in marker:
                    x, y = i.coords
                    canvas.create_rectangle(x, y, x + 5, y + 5, fill=i.color)
            else:
                x, y = marker.coords
                canvas.create_rectangle(x, y, x + 5, y + 5, fill=marker.color)
    else:
        x, y = markers.coords
        canvas.create_rectangle(x, y, x + 5, y + 5, fill=markers.color)


# creates and returns a canvas of entered background color
def CreateMap(root, canvasBackground):

    canvas = tk.Canvas(right, bg=canvasBackground, width=850, height=800, highlightthickness=0)

    canvas.grid(row=0, column=0, sticky="") 
    right.grid_rowconfigure(0, weight=1) 
    right.grid_columnconfigure(0, weight=1) 

    return canvas


# returns location and path markers from the coords entered in the coords.txt file
def GetMarkersFromFile(file):
    locationMarkers = []
    pathMarkers = []

    locationMarkerCoords, locationMarkersNames, pathMarkerCoords = ParseFile(file)

    for i in range(len(locationMarkerCoords)):
        locationMarkers.append(LocationMarker(locationMarkerCoords[i], name=locationMarkersNames[i]))

    for i in pathMarkerCoords:
        temp = []

        for j in i:
            temp.append(PathMarker(j))
        pathMarkers.append(temp)

    return locationMarkers, pathMarkers


# uses Djikstra's algo to find the shortest path between two coords from the graph
def GetPathLength(graph, start_coords, end_coords):

    # Priority queue to store (current distance, node) tuples
    to_visit = [(0, start_coords)]

    # Dictionary to keep track of the shortest distance to each node
    shortest_distances = {start_coords: 0}

    # Dictionary to keep track of the predecessor of each node in the shortest path
    predecessors = {}

    while to_visit:
        # Pop the node with the smallest distance from the queue
        current_dist, current_node = heapq.heappop(to_visit)

        # If we reach the destination node, reconstruct the path
        if current_node == end_coords:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = predecessors.get(current_node)
            path.reverse()  
            return current_dist, path

        # Explore neighbors of the current node
        for neighbor, length in graph[current_node].items():
            
            # Calculate the distance to this neighbor
            new_dist = current_dist + length

            # If the calculated distance is shorter, update the shortest distance and add to the queue
            if neighbor not in shortest_distances or new_dist < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_dist
                predecessors[neighbor] = current_node 
                heapq.heappush(to_visit, (new_dist, neighbor))

    return None, None  # If there's no path


# returns the straight line distance between two coords
def GetDistance(coords1, coords2):
    x1, y1 = coords1
    x2, y2 = coords2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# converts the path markers into a graph format
def BuildGraph(pathMarkerList):
    graph = {}

    for path in pathMarkerList:
        for i in range(len(path) - 1):
            coords1 = path[i].coords
            coords2 = path[i+1].coords
            distance = round(GetDistance(coords1, coords2), 2)

            if coords1 not in graph:
                graph[coords1] = {}
            if coords2 not in graph:
                graph[coords2] = {}

            graph[coords1][coords2] = distance
            graph[coords2][coords1] = distance
    
    return graph


# highlights the entered path
def HighlightPath(path):
    
    for i in range(len(path) - 1):
        map.create_line(
            path[i], path[i + 1], fill="blue", width=3)

# unhighlights the entered path
def UnhighlightPreviousPath(path):
    for i in range(len(path) - 1):
        map.create_line(
            path[i], path[i + 1], fill="black", width=3)


# Returns the coords of a marker from its name
def GetCoordsFromName(name):
    global locationMarkersList
    for i in locationMarkersList:
        if i.name.strip() == name:
            return i.coords

# update map with the new coords
def UpdateMap(a, b):

    global previousPath
    UnhighlightPreviousPath(previousPath)

    path = []
    distance, path = GetPathLength(graph, GetCoordsFromName(a), GetCoordsFromName(b))
    previousPath = path

    HighlightPath(path)

# root window
root = tk.Tk("Nav_sys")

root.geometry("850x800")
root.title("Campus Navigation System")
root.state("zoomed")
# root.attributes("-fullscreen", True)


# paths handling using os
cwd = os.getcwd()
file = os.path.join(cwd, "coords.txt")

backgroundImagePath = os.path.join(cwd, "map.png")
backgroundImage = tk.PhotoImage(file = backgroundImagePath)


#*---------------------------------------------------------------------------------------------------------------------------

#Custom font
cusfont = tkfont.Font(family="Aptos", size=14)

# Container frame
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True, side="left")

# Main grid configuration
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)

# Left frame in main frame
left = tk.Frame(main_frame, width=300, height=800, bg="black")
left.grid(row=0, column=0, sticky="nswe")

# Right frame in main frame
right = tk.Frame(main_frame, width=850, height=800, bg="#3e3f43")
right.grid(row=0, column=1, sticky="nswe")

# Dropdown menu
def dropdown():
    global ask, sel, menu, confirmbutton, placeholder
    global ask0, sel0, menu0, placeholder0
    
    #starting point menu
    options = ["AB1", "AB2", "AB3", "Library", "Canteen", "Main Office", "Post Office"]
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

    #confirm button
    confirmbutton = ttk.Button(left, text="Confirm selection", command=clconfirmbutton)
    confirmbutton.place(relx=0.5, rely=0.6, anchor="center")

# Creating home button
def crhomebutton():
    global backbutton
    backbutton = ttk.Button(left, text="Home", command=clbackbutton)
    backbutton.place(relx=0.5, rely=0.9, anchor="center")

# Clicking home button
def clbackbutton():
    resetui()
    dropdown()
    crhistorrybutton()
    crhomebutton()

# Creating history button
def crhistorrybutton():
    global historybutton  
    historybutton = ttk.Button(left, text="View history", command=clhistorybutton)
    historybutton.place(relx=0.5, rely=0.7, anchor="center")

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

# Creating clear history button
def crclrhistorybutton():
    global clrhistorybutton  
    clrhistorybutton = ttk.Button(left, text="Clear history", command=clclrhistorybutton)
    clrhistorybutton.place(relx=0.5, rely=0.7, anchor="center")

# Clicking clear history button
def clclrhistorybutton():
    with open("history.txt", "w") as file:
        pass
    log.config(text="History cleared")
    clrhistorybutton.destroy()

selopt = None
startopt = None

# Clicking confirm button
def clconfirmbutton():
    global selopt, startopt
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

    if not (startopt == "" or selopt == ""):
        UpdateMap(startopt, selopt)

    global disp
    disp = ttk.Label(left, text=disp_text, font=cusfont, background="black", foreground="white")
    disp.place(relx=0.5, rely=0.4, anchor="center")

    crhomebutton()
    crhistorrybutton()

# Reset user interface
def resetui():
    for widget in left.winfo_children():
        widget.destroy()

#Start function
def start():
    dropdown()
    crhomebutton()
    crhistorrybutton()

#*---------------------------------------------------------------------------------------------------------------------------

map = CreateMap(root, "black")
map.create_image(0, 0, anchor="nw", image=backgroundImage)




locationMarkersList, pathMarkerList = GetMarkersFromFile(file)

graph = BuildGraph(pathMarkerList)
previousPath = []

# DrawMarkers(locationMarkersList, map)
# DrawMarkers(pathMarkerList, map)

root.bind("<Escape>", CloseWindow)

start()

root.mainloop()
