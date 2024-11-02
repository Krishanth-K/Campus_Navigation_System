def ParseFile(filePath):

    locationMarkerCoords = []
    PathMarkerCoords = []

    with open(filePath, "r") as file:
        lines = file.readlines()

        for i, line in enumerate(lines):

            if line.startswith("Location:"):
                if i + 1 < len(lines):
                    coordsLine = lines[i + 1].strip()
                    coordsLine = coordsLine.removeprefix("(").removesuffix(")").strip()
                    # print(coordsLine)
                    coord = tuple(map(int, coordsLine.split(", ")))

                    locationMarkerCoords.append(coord)

            if line.startswith("Path"):
                pathCoords = []

                if i + 1 < len(lines):
                    coordsLine = lines[i + 1].strip()
                    coordsLine = coordsLine.removeprefix("(").removesuffix(")").strip()
                    # print(coordsLine)
                    coord = tuple(map(int, coordsLine.split(", ")))

                    pathCoords.append(coord)

                c = i + 2
                while c < len(lines) and lines[c].startswith("("):
                    coordsLine = lines[c].strip()
                    coordsLine = coordsLine.removeprefix("(").removesuffix(")").strip()
                    # print(coordsLine)
                    coord = tuple(map(int, coordsLine.split(", ")))

                    pathCoords.append(coord)
                    c += 1

                PathMarkerCoords.append(pathCoords)

    return locationMarkerCoords, PathMarkerCoords

ParseFile("coords.txt")
