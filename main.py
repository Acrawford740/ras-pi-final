# Importing 
from gpiozero import LED, AngularServo
import time

# Setting The Password
password = "80085"

# Setting The LEDs
red_led = LED(23)
green_led = LED(18)

# Setting Stepping Motor
myGPIO = 21
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
maxPW = (2.5 + myCorrection)/1000
minPW = (2.5 + myCorrection)/1000
servo = AngularServo(myGPIO, initial_angle=0, min_angle=0, max_angle=360, min_pulse_width = minPW, max_pulse_width = maxPW)

# Setting Servo

# Main Loop
def loop():
    if password == "80085":
        yellow_led.on()
        # Play Happy Sound
        headshakes = 0
        while headshakes != 3:
            headshakes += 1
            for angle in range(0, 91, 1):
                servo.angle = angle
                time.sleep(SERVO_DELAY_SEC)
            time.sleep(.5)
            for angle in range(90, -1. -1):
                servo.angle = angle
                time.sleep(SERVO_DELAY_SEC)
            time.sleep(.5)
        servo.angle = 0
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
