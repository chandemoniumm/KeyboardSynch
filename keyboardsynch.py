import time
from openrgb import OpenRGBClient, utils
from openrgb.utils import RGBColor
from PIL import ImageGrab

def get_avg_screen_color():
    img = ImageGrab.grab()
    img = img.resize((50, 50))
    pixels = img.getdata()
    r = g = b = 0
    count = 0
    for pixel in pixels:
        r += pixel[0]
        g += pixel[1]
        b += pixel[2]
        count += 1
    return (r // count, g // count, b // count)

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

try:
    while True:
        try:
            r, g, b = get_avg_screen_color()
            color = RGBColor(r, g, b)
            keyboard.set_color(color)
            
        except utils.OpenRGBDisconnected:
            print("Lost connection to OpenRGB, reconnecting...")
            client = connect_openrgb()
            keyboard = client.devices[0]
except KeyboardInterrupt:
    print("Exiting...")
    client.disconnect()
