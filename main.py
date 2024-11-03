import tkinter as tk
import os
from parser import ParseFile
from math import sqrt


# markers are "location pins" on the map
class Marker():
    def __init__(self, coords, color="Red"):
        self.coords = coords
        self.color = color

    # returns the distance between a marker and other along a straight line
    def GetLineDistance(self, other):

        if not isinstance(Marker):
            raise Exception("Not an instance of Marker")

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


def CreatePathsFromMarkers(pathMarkers, map):
    paths = []

    # i is a single list of pathMarkers
    for marker in pathMarkers:

        temp = []
        for j in range(len(marker) - 1):
            line = map.create_line(marker[j].coords, marker[j + 1].coords, fill = "white")
            
            paths.append(line)

        paths.append(temp)

    return paths


# root window
root = tk.Tk("Nav_sys")

root.geometry("800x600")
root.title("Campus Navigation System")

# paths handling using os
cwd = os.getcwd()
file = os.path.join(cwd, "coords.txt")

map = CreateMap(root, "black")

locationMarkers, pathMarkers = GetMarkersFromFile(file)
# print(pathMarkers)
paths = CreatePathsFromMarkers(pathMarkers, map)

DrawMarkers(locationMarkers, map)
DrawMarkers(pathMarkers, map)

root.mainloop()
