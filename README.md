
# Campus Navigation System

This project is a **Campus Navigation System** built in Python with a GUI interface using **Tkinter**. The system allows users to select a starting point and destination from a dropdown menu, displaying the shortest path between them on a campus map. This project uses **Dijkstra's Algorithm** for efficient pathfinding and reads coordinates from an external file, making it customizable for different campus layouts.

## Features

- **Marker Display**: Visualizes important campus locations and paths on a map.
- **Shortest Path Calculation**: Uses Dijkstra's Algorithm to determine and highlight the shortest route between two selected points.
- **History Log**: Records previously selected routes with an option to view or clear the history.
- **Dropdown Menu**: Easy selection of starting and ending points from a predefined list of locations.
- **Customizable Map and Coordinates**: Loads coordinates from an external file (`coords.txt`), enabling easy customization for different maps and locations.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python installations)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. Place the `coords.txt` file in the project directory. This file should contain coordinates and path definitions.

3. Run the main script:
   ```bash
   python main.py
   ```

### File Structure

- `main.py`: Main script to run the navigation system.
- `coords.txt`: Contains location and path coordinates for map markers.
- `map.png`: Map background image used in the canvas display.
- `history.txt`: Stores history of previous routes selected.

### Customizing `coords.txt`

The `coords.txt` file should follow this structure:
- Locations:
  ```
  Location: <Location Name>
  (x, y) # Optional Description
  ```
- Paths:
  ```
  Path: <Path Name>
  (x1, y1)
  (x2, y2)
  ...
  ```

## How It Works

1. **Loading Coordinates**: The `ParseFile` function reads location and path coordinates from `coords.txt` and organizes them into lists.
2. **Pathfinding**: `GetPathLength` calculates the shortest path using Dijkstra’s algorithm, leveraging the parsed data as nodes and edges in a graph.
3. **UI Components**: Tkinter is used to build the UI, with buttons, dropdowns, and dynamic path highlighting.

## Future Enhancements

- Real-time GPS integration for live location tracking.
- Expanded map customization with zoom and pan functionalities.
- Improved pathfinding algorithms to handle larger maps.
