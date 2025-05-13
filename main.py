# Importing 
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

# Setting The Pins For The Seven Segment Display
segments = {
    'A': LED(),
    'B': LED(),
    'C': LED(),
    'D': LED(),
    'E': LED(),
    'F': LED(),
    'G': LED()
}

# Setting The Digits
digits = {
    '0': ['A', 'B', 'C', 'D', 'E', 'F'],
    '1': ['B', 'C'],
    '2': ['A', 'B', 'D', 'E', 'G'],
    '3': ['A', 'B', 'C', 'D', 'G'],
    '4': ['B', 'C', 'F', 'G'],
    '5': ['A', 'C', 'D', 'F', 'G'],
    '6': ['A', 'C', 'D', 'E', 'F', 'G'],
    '7': ['A', 'B', 'C'],
    '8': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    '9': ['A', 'B', 'C', 'F', 'G']
}

# Main Loop
def loop():
    

# Close All
def destroy():
    left_button.close()
    right_button.close()
    top_button.close()
    bottom_button.close()
    red_led.close()
    yellow_led.close()

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()