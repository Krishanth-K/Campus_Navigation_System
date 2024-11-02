import tkinter as tk
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
    pass

class PathMarker(Marker):
    pass


def DrawMarkers(markers, canvas):

    if isinstance(markers, list):
        for marker in markers:
            x, y = marker.coords
            canvas.create_rectangle(x, y, x + 5, y + 5, fill=marker.color, outline="red")
            print("list")

    else:
        x, y = markers.coords
        canvas.create_rectangle(x, y, x + 5, y + 5, fill=markers.color, outline="red")
        print("not list")

def CreateMap(root, canvasBackground):
    canvas = tk.Canvas(root, bg = canvasBackground)
    canvas.pack(fill = tk.BOTH, expand = True)

    return canvas


root = tk.Tk("Nav_sys")

root.geometry("800x600")
root.title("Campus Navigation System")

map = CreateMap(root, "black")

markers = []

markers.append(PathMarker((200, 200)))
markers.append(PathMarker((100, 300), "green"))

DrawMarkers(markers, map)

root.mainloop()
