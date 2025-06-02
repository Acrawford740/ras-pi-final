# Importing 
from gpiozero import LED, Button
import time

# Set The Password People Are Trying To Input
password = "80085"

# Set The Buttons
left_button = Button()
right_button = Button()
top_button = Button()
bottom_button = Button()

# Set The LEDs
red_led = LED()
yellow_led = LED()

# Setting Stepping Motor


# Setting Servo

# Setting The LCD Board

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
    if password == "Good":
        yellow_led.on()
        # Play Happy Sound
        headshakes = 0
        while headshakes != 3:
            headshakes += 1
            # Nod Up Servo
            time.sleep(.5)
            # Nod Down Servo
            time.sleep(.5)
        #Center Head
        yellow_led.off()
    else:
        red_led.on()
        headshakes = 0
        while headshakes != 3:
            headshakes += 1
            # Nod Left Stepping
            time.sleep(.5)
            # Nod Right Stepping
            time.sleep(.5)
        # Center Head
        red_led.off()

# Close All
def destroy():
    left_button.close()
    right_button.close()
    top_button.close()
    bottom_button.close()
    red_led.close()
    yellow_led.close()
    # Close Servo
    # Close Stepping Motor

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
