import os
import time

# Set the path to the output file
output_file = "window_sizes.csv"

# Define a function to get the size of the active window using xdotool
def get_window_size():
    size_str = os.popen("xdotool getactivewindow getwindowgeometry | grep 'Geometry'").read()
    size_arr = size_str.strip().split("+")[0].split("x")
    width = int(size_arr[0])
    height = int(size_arr[1])
    return width, height

# Write the header to the output file
with open(output_file, "w") as f:
    f.write("width,height\n")

# Loop to collect data
while True:
    # Get the size of the active window
    width, height = get_window_size()
    # Append the data to the output file
    with open(output_file, "a") as f:
        f.write("{},{}\n".format(width, height))
    # Wait for 0.1 seconds before checking again
    time.sleep(0.1)
