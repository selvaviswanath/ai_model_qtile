import csv
import time
import qtile

# Define the path to the CSV file
csv_path = "/path/to/layout_dataset.csv"

# Define the headers for the CSV file
headers = ["timestamp", "app1_pos", "app1_size", "app2_pos", "app2_size"]

# Define the layout for your applications
# This is an example of a two-pane layout with two applications
layout = [
    {
        "name": "app1",
        "position": (0, 0),
        "size": (800, 600)
    },
    {
        "name": "app2",
        "position": (800, 0),
        "size": (800, 600)
    }
]

def get_layout():
    # Get the current workspace object
    workspace = qtile.current_screen().group

    # Get the layout object for the current workspace
    layout = workspace.layout

    # Define a list to hold the position and size of each window
    window_positions = []

    # Loop through each window in the workspace
    for i, window in enumerate(workspace.windows):
        # Get the position and size of the window
        position = (window.x, window.y)
        size = (window.width, window.height)

        # Add the position and size to the list
        window_positions.append((position, size))

    # Return the list of window positions
    return window_positions

# Create the CSV file and write the headers
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

# Continuously record the layout information and append it to the CSV file
while True:
    # Get the current time
    timestamp = int(time.time())

    # Get the current layout
    app_positions = []
    for app in layout:
        app_name = app["name"]
        app_position = get_layout()[i][0]
        app_size = get_layout()[i][1]
        app_positions.extend([app_name, app_position, app_size])

    # Write the layout information to the CSV file
    with open(csv_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp] + app_positions)

    # Wait for a specified interval before recording the next layout
    time.sleep(60)  # Wait for 60 seconds