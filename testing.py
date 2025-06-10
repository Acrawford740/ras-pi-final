from gpiozero import AngularServo
import time

GPIOside = 24
GPIOup = 18
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
maxPW = (2.5 + myCorrection)/1000
minPW = (0.5 - myCorrection)/1000
servoUp = AngularServo(GPIOup, initial_angle=0, min_angle=-180, max_angle=180, min_pulse_width = minPW, max_pulse_width = maxPW)
servoSide = AngularServo(GPIOside, initial_angle=0, min_angle=-180, max_angle=180, min_pulse_width = minPW, max_pulse_width = maxPW)

def nodNo():
    timesNO = 0
    while timesNO != 5:
        timesNO += 1
        servoSide.angle = 40
        time.sleep(1)
        servoSide.angle = -40
        time.sleep(1)
    servoSide.angle = 0

def nodYes():
    timesYes = 0
    while timesYes != 5:
        timesYes += 1
        servoUp.angle = 10
        time.sleep(1)
        servoUp.angle = -80
        time.sleep(1)
    servoUp.angle = 5

def main():
    nodNo()
    time.sleep(3)
    nodYes()
    time.sleep(3)

def destroy():
    servoUp.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()