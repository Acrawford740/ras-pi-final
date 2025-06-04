# Importing 
from gpiozero import LED, AngularServo
import time

# Setting The Password
password = "80085"

# Setting The LEDs
red_led = LED(23)
green_led = LED(18)

# Setting Servo
myGPIO = 21
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
maxPW = (2.5 + myCorrection)/1000
minPW = (2.5 + myCorrection)/1000
servo = AngularServo(myGPIO, initial_angle=0, min_angle=0, max_angle=360, min_pulse_width = minPW, max_pulse_width = maxPW)

# Setting Stepping Motor
motorPins = (24, 12, 16, 20)
motors = list(map(lambda pin: OutputDevice(pin), motorPins))
CCWStep = (0x01, 0x02, 0x04, 0x08)
CWStep = (0x01, 0x02, 0x04, 0x08)

def nodYes():
    for angle in range(0, 91, 1):
        servo.angle = angle
        time.sleep(SERVO_DELAY_SEC)
    time.sleep(.5)
    for angle in range(90, -1. -1):
        servo.angle = angle
        time.sleep(SERVO_DELAY_SEC)
        time.sleep(.5)
    servo.angle = 0

def nodNo():
    pass

# Main Loop
def main():
    if password == "80085":
        yellow_led.on()
        # Play Happy Sound
        headshakes = 0
        while headshakes != 3:
            headshakes += 1
            nodYes()
        yellow_led.off()
    else:
        red_led.on()
        headshakes = 0
        while headshakes != 3:
            headshakes += 1
            nodNo()
        # Center Head
        red_led.off()

# Close All
def destroy():
    red_led.close()
    green_led.close()
    servo.close()
    

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
