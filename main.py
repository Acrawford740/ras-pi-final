# Importing 
from gpiozero import LED
import time

# Set The Password People Are Trying To Input
password = "80085"

# Set The LEDs
red_led = LED(23)
green_led = LED(18)

# Setting Stepping Motor


# Setting Servo

# Main Loop
def loop():
    if password == "80085":
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
    red_led.close()
    yellow_led.close()
    # Close Servo
    # Close Stepping Motor

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
