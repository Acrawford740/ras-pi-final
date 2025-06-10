from gpiozero import AngularServo
import time

GPIOup = 18
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
maxPW = (2.5 + myCorrection)/1000
minPW = (0.5 - myCorrection)/1000
servoUp = AngularServo(GPIOup, initial_angle=0, min_angle=-180, max_angle=180, min_pulse_width = minPW, max_pulse_width = maxPW)

def nodYes():
    timesYes = 0
    while timesYes != 5:
        timesYes += 1
        servoUp.angle = 10
        time.sleep(1)
        servoUp.angle = -80
        time.sleep(1)
    servoUp.angle = 5

def destroy():
    servoUp.close()

if __name__ == "__main__":
    try:
        nodYes()
    except KeyboardInterrupt:
        destroy()