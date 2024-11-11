import os
import heapq
import tkinter as tk
from parser import ParseFile
from math import sqrt


# markers are "location pins" on the map
class Marker():
    def __init__(self, coords, color="Red"):
        self.coords = coords
        self.color = color

    # returns the distance between a marker and other along a straight line
    def GetLineDistance(self, other):

        # if not isinstance(Marker):
        #     raise Exception("Not an instance of Marker")

        x1, y1 = self.coords
        x2, y2 = other.coords

        distance = sqrt((x2 - x1)**2 + (y2-y1)**2)

        return distance


# subclass of Marker with default color as blue
class LocationMarker(Marker):
    def __init__(self, coords, color="blue"):
        super().__init__(coords, color)


# subclass of Marker with default color as green
class PathMarker(Marker):
    def __init__(self, coords, color="red"):
        super().__init__(coords, color)


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
    canvas = tk.Canvas(root, bg=canvasBackground)
    canvas.pack(fill=tk.BOTH, expand=True)
    # canvas.grid_configure()

    return canvas


# returns location and path markers from the coords entered in the coords.txt file
def GetMarkersFromFile(file):
    locationMarkers = []
    pathMarkers = []

    locationMarkerCoords, pathMarkerCoords = ParseFile(file)

    for i in locationMarkerCoords:
        locationMarkers.append(LocationMarker(i))

    for i in pathMarkerCoords:
        temp = []

        for j in i:
            temp.append(PathMarker(j))
        pathMarkers.append(temp)

    return locationMarkers, pathMarkers


def DrawPathsFromMarkers(pathMarkers, map, lineWidth=3):

    # i is a single list of pathMarkers
    for marker in pathMarkers:

        for j in range(len(marker) - 1):
            map.create_line(
                marker[j].coords, marker[j + 1].coords, fill="white", width=lineWidth)


def GetLineDistance(mark1, mark2):

    if not isinstance(mark1, Marker) and isinstance(mark2, Marker):
        raise Exception("Not an instance of Marker")

    return mark1.GetLineDistance(mark2)


#? HOW DOES THIS WORK

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
            path.reverse()  # Reverse to get the path from start to end
            return current_dist, path

        # Explore neighbors of the current node
        for neighbor, length in graph[current_node].items():
            # Calculate the distance to this neighbor
            new_dist = current_dist + length

            # If the calculated distance is shorter, update the shortest distance and add to the queue
            if neighbor not in shortest_distances or new_dist < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_dist
                predecessors[neighbor] = current_node  # Track the predecessor for path reconstruction
                heapq.heappush(to_visit, (new_dist, neighbor))

    return None, None  # If there's no path


def GetDistance(coords1, coords2):
    x1, y1 = coords1
    x2, y2 = coords2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


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


def HighlightPath(path):
    
    for i in range(len(path) - 1):
        map.create_line(
            path[i], path[i + 1], fill="blue", width=3)

# root window
root = tk.Tk("Nav_sys")

root.geometry("850x800")
root.title("Campus Navigation System")


# paths handling using os
cwd = os.getcwd()
file = os.path.join(cwd, "coords.txt")

backgroundImagePath = os.path.join(cwd, "map.png")
backgroundImage = tk.PhotoImage(file = backgroundImagePath)

map = CreateMap(root, "black")
map.create_image(0, 0, anchor="nw", image=backgroundImage)

#!---------------------------------------------------------------------------------------------------------------------------

def PrintCoords(event):
    print(f"({event.x}, {event.y})")


map.bind("<Button-1>", PrintCoords)

#!---------------------------------------------------------------------------------------------------------------------------

locationMarkers, pathMarkerList = GetMarkersFromFile(file)
DrawPathsFromMarkers(pathMarkerList, map)


graph = BuildGraph(pathMarkerList)

distance, path = GetPathLength(graph, (623, 695), (479, 361))
print(distance)
print(path)

HighlightPath(path)

DrawMarkers(locationMarkers, map)
DrawMarkers(pathMarkerList, map)

root.bind("<Escape>", CloseWindow)

root.mainloop()
