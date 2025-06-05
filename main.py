# Importing 
from gpiozero import LED, AngularServo
from playsound import playsound
import time

# Setting The LEDs
red_led = LED(23)
green_led = LED(18)

# Setting Servo Up
GPIOup = #
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
maxPW = (2.5 + myCorrection)/1000
minPW = (2.5 + myCorrection)/1000
servoUp = AngularServo(GPIOup, initial_angle=0, min_angle=0, max_angle=360, min_pulse_width = minPW, max_pulse_width = maxPW)

# Settign Servo Sideways
GPIOside = #
servoSide = AngularServo(GPIOside, initial_angle=0, min_angle=0, max_angle=360, min_pulse_width=minPW, max_pulse_width=maxPW)

def nodYes():
    for angle in range(0, 91, 1):
        servoUp.angle = angle
        time.sleep(SERVO_DELAY_SEC)
    time.sleep(.5)
    for angle in range(90, -1. -1):
        servoUp.angle = angle
        time.sleep(SERVO_DELAY_SEC)
    time.sleep(.5)
    servoUp.angle = 0

def nodNo():
    for angle in range(0, 126, 1):
        servoSide.angle = angle
        time.sleep(SERVO_DELAY_SEC)
    time.sleep(.5)
    for angle in range(126, -40, -1):
        servoSide.angle = angle
        time.sleep(SERVO_DELAY_SEC)
    time.sleep(.5)
    servoSide.angle = 0

def correct():
    green_led.on()
    playsound()
    time.sleep(3)
    green_led.off()

def incorrect():
    red_led.on()
    # play audio
    time.sleep(3)
    red_led.off()

# Main Loop
def main():
    if password == "80085":
        correct()
        headshakes = 0
        while headshakes != 3:
            headshakes += 1
            nodYes()
    else:
        incorrect()
        headshakes = 0
        while headshakes != 3:
            headshakes += 1
            nodNo()

# Close All
def destroy():
    red_led.close()
    green_led.close()
    servoUp.close()
    servoSide.close()
    

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
