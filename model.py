import csv
from Xlib import display
import subprocess
import time
from qtile import ipc
client = ipc.Client()
def get_window_info(window):
    geometry = window.get_geometry()
    position = window.get_attributes().get('map_state')
    if position == 'IsViewable':
        x, y = geometry.x, geometry.y
        width, height = geometry.width, geometry.height
        return x, y, width, height
    else:
        return None

def write_to_csv(window_info):
    with open('window_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(window_info)

while True:
    root = display.Display().screen().root
    window_ids = root.get_full_property(
        display.Display().intern_atom('_NET_CLIENT_LIST'), display.X.AnyPropertyType).value
    for window_id in window_ids:
        window = client.window(window_id)
        info = get_window_info(window)
        if info is not None:
            write_to_csv(info)
    time.sleep(1)