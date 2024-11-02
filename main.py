import tkinter as tk
import os
from parser import ParseFile
from math import sqrt


class Marker():
    def __init__(self, coords, color = "Red"):
        self.coords = coords
        self.color = color

    def GetLineDistance(self, other):
        
        if not isinstance(Marker):
            raise Exception("Not an instance of Marker")

        x1, y1 = self.coords
        x2, y2 = other.coords

        distance = sqrt( (x2 - x1)**2 + (y2-y1)**2)

        return distance


class LocationMarker(Marker):
    def __init__(self, coords, color = "blue"):
        super().__init__(coords, color)

class PathMarker(Marker):
    def __init__(self, coords, color = "green"):
        super().__init__(coords, color)


def DrawMarkers(markers, canvas):

    if isinstance(markers, list):
        for marker in markers:
            x, y = marker.coords
            canvas.create_rectangle(x, y, x + 5, y + 5, fill=marker.color)

    else:
        x, y = markers.coords
        canvas.create_rectangle(x, y, x + 5, y + 5, fill=markers.color)

def CreateMap(root, canvasBackground):
    canvas = tk.Canvas(root, bg = canvasBackground)
    canvas.pack(fill = tk.BOTH, expand = True)

    return canvas

def GetMarkersFromFile(file):
    locationMarkerCoords, pathMarkerCoords = ParseFile(file)
    locationMarkers = []
    pathMarkers = []

    for i in locationMarkerCoords:
        locationMarkers.append(LocationMarker(i))
    for i in pathMarkerCoords:
        for j in i:
            pathMarkers.append(PathMarker(j))

    return locationMarkers, pathMarkers


root = tk.Tk("Nav_sys")

root.geometry("800x600")
root.title("Campus Navigation System")

cwd = os.getcwd()
file = os.path.join(cwd, "coords.txt")

map = CreateMap(root, "black")

locationMarkers, pathMarkers = GetMarkersFromFile(file)

DrawMarkers(locationMarkers, map)
DrawMarkers(pathMarkers, map)

root.mainloop()
