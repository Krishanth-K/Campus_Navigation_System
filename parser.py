# returns the location and path coords by parsing the file
def ParseFile(filePath):

    locationMarkerCoords = []
    PathMarkerCoords = []

    with open(filePath, "r") as file:
        lines = file.readlines()

        # i is the index of the line
        for i, line in enumerate(lines):

            if line.startswith("--"):
                continue            

            if line.startswith("Location:"):
                # check if next line exists
                if i + 1 < len(lines):
                    coordsLine = lines[i + 1].strip()
                    coordsLine = coordsLine.removeprefix("(").removesuffix(")").strip()
                    # print(coordsLine)
                    #convert the integers into a tuple
                    coord = tuple(map(int, coordsLine.split(", ")))

                    locationMarkerCoords.append(coord)

            if line.startswith("Path"):
                pathCoords = []

                # check if next line exists
                if i + 1 < len(lines):
                    coordsLine = lines[i + 1].strip()
                    coordsLine = coordsLine.removeprefix("(").removesuffix(")").strip()
                    # print(coordsLine)
                    #convert the integers into a tuple
                    coord = tuple(map(int, coordsLine.split(", ")))

                    pathCoords.append(coord)

                # continue adding the next line until it is not a coordinate
                c = i + 2
                while c < len(lines) and lines[c].startswith("("):
                    coordsLine = lines[c].strip()
                    coordsLine = coordsLine.removeprefix("(").removesuffix(")").strip()
                    # print(coordsLine)

                    #convert the integers into a tuple
                    coord = tuple(map(int, coordsLine.split(", ")))

                    pathCoords.append(coord)
                    c += 1

                PathMarkerCoords.append(pathCoords)

    return locationMarkerCoords, PathMarkerCoords