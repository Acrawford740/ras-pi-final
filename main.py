from gpiozero import LED, Button
import time
import random

# Set The Buttons
left_button = Button(24)
right_button = Button(23)
top_button = Button(25)
bottom_button = Button(27)
# Set The LEDs
red_led = LED(26)
yellow_led = LED(4)

# Main Loop
def loop():
    pass

# Close All
def destroy():
    left_button.close()
    right_button.close()
    top_button.close()
    bottom_button.close()
    red_led.close()
    yellow_led.close()