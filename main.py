import os
import pprint
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from parser import ParseFile
from math import sqrt
from collections import defaultdict


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
    paths = []

    # i is a single list of pathMarkers
    for marker in pathMarkers:

        temp = []
        for j in range(len(marker) - 1):
            line = map.create_line(
                marker[j].coords, marker[j + 1].coords, fill="white", width=lineWidth)

            paths.append(line)

        paths.append(temp)


def GetLineDistance(mark1, mark2):

    if not isinstance(mark1, Marker) and isinstance(mark2, Marker):
        raise Exception("Not an instance of Marker")

    return mark1.GetLineDistance(mark2)


def GetPathLength(graph, startCoords, endCoords):
    visited = set()
    toVisit = [(startCoords, 0)]

    while (toVisit):

        current, dist = toVisit.pop(0)

        if current == endCoords:
            return dist

        visited.add(current)

        for neighbor, length in graph[current].items():
            if neighbor not in visited:
                toVisit.append((neighbor, dist + length))

    return None


def GetJunctions(pathMarkers):

    junctions = defaultdict(list)

    for pathIndex, path in enumerate(pathMarkers):

        for marker in path:
            # adding all coordinates as keys and the index as values
            junctions[marker.coords].append(pathIndex)

    # removing all non junction coords
    junctions = {coords: paths for coords, paths in junctions.items() if len(paths) > 1} # think of paths as the count of paths

    return junctions


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


# root window
root = tk.Tk("Nav_sys")

root.geometry("800x600")
root.title("Campus Navigation System")


# paths handling using os
cwd = os.getcwd()
file = os.path.join(cwd, "coords.txt")

map = CreateMap(root, "black")

locationMarkers, pathMarkerList = GetMarkersFromFile(file)
DrawPathsFromMarkers(pathMarkerList, map)

graph = BuildGraph(pathMarkerList)
pprint.pprint(graph)

# junctions = GetJunctions(pathMarkerList)
# print(junctions)

distance = GetPathLength(graph, (100, 100), (300, 200))
print(distance)

DrawMarkers(locationMarkers, map)
DrawMarkers(pathMarkerList, map)


root.bind("<Escape>", CloseWindow)

root.mainloop()
