import time
from openrgb import OpenRGBClient, utils
from openrgb.utils import RGBColor
from PIL import ImageGrab

def get_center_box_avg_color(box_size=50):
    img = ImageGrab.grab()
    width, height = img.size

    left = max((width // 2) - (box_size // 2), 0)
    top = max((height // 2) - (box_size // 2), 0)
    right = min(left + box_size, width)
    bottom = min(top + box_size, height)

    center_box = img.crop((left, top, right, bottom))
    pixels = center_box.getdata()

    r = g = b = 0
    count = 0
    for pixel in pixels:
        r += pixel[0]
        g += pixel[1]
        b += pixel[2]
        count += 1

    return (r // count, g // count, b // count)

def interpolate_color(c1, c2, factor):
    r = int(c1[0] + (c2[0] - c1[0]) * factor)
    g = int(c1[1] + (c2[1] - c1[1]) * factor)
    b = int(c1[2] + (c2[2] - c1[2]) * factor)
    return (r, g, b)

def connect_openrgb():
    while True:
        try:
            client = OpenRGBClient()
            print("Connected to OpenRGB SDK server.")
            return client
        except Exception as e:
            print(f"Failed to connect to OpenRGB: {e}. Retrying in 5 seconds...")
            time.sleep(5)

client = connect_openrgb()
keyboard = client.devices[0]

current_color = (0, 0, 0)  # Start with black/off

try:
    while True:
        target_color = get_center_box_avg_color(50)  # Sampling 50x50 box at center
        steps = 2
        for i in range(1, steps + 1):
            interp_color = interpolate_color(current_color, target_color, i / steps)
            keyboard.set_color(RGBColor(*interp_color))
            time.sleep(0.05)
        current_color = target_color
except KeyboardInterrupt:
    print("Exiting...")
    client.disconnect()
