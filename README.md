Keyboard Screen Color Sync

This Python script dynamically syncs your keyboard backlight color with the average color displayed on your screen, creating an immersive lighting effect. It uses the OpenRGB SDK to control RGB-enabled keyboards on Linux systems. The script captures the average color of your screen every second, updates the keyboard backlight color to match the screen color in real-time, and automatically reconnects to the OpenRGB SDK server if the connection is lost.

Requirements include a Linux system with an RGB-enabled keyboard supported by OpenRGB, OpenRGB installed and running with the SDK server enabled, Python 3.x, and the Python packages `openrgb-python` and `pillow`. To install dependencies, run `pip install openrgb-python pillow`. 

To use the script, ensure OpenRGB is running with the SDK server enabled, then run the script with elevated permissions using `sudo python3 keyboardsynch.py` since root access might be necessary for hardware control. The script captures a screenshot, downsizes it for performance, calculates the average RGB color, and sends the color update to the keyboard every second. If the connection to OpenRGB is lost, it attempts to reconnect automatically.

The project is licensed under the MIT License.
