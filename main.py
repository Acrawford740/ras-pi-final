# Importing 
from gpiozero import LED, Button
import time

# Set The Password People Are Trying To Input
password = ""

# Set The Buttons
left_button = Button()
right_button = Button()
top_button = Button()
bottom_button = Button()

# Set The LEDs
red_led = LED()
yellow_led = LED()

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

# Making The Speakers Do The Angry Sound

# Making The Speakers Do The Happy Sound

# Creating The Button Functions
def LeftPushed():
    pass

def RightPushed():
    pass

def TopPushed():
    pass

def BottomPushed():
    pass

# Main Loop
def loop():
    if password == "IDK":
        yellow_led.on()
    else:
        red_led.on()
        time.sleep(1)
        red_led.off()

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
