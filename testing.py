from gpiozero import AngularServo
import time

GPIOside = 18
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
maxPW = (2.5 + myCorrection)/1000
minPW = (0.5 - myCorrection)/1000
servoSide = AngularServo(GPIOside, initial_angle=0, min_angle=-180, max_angle=180, min_pulse_width = minPW, max_pulse_width = maxPW)

def nodNo():
    times = 0
    while times != 5:
        times += 1
        servoSide.angle = 40
        time.sleep(1)
        servoSide.angle = -40
        time.sleep(1)
    servoSide.angle = 0

def incorrect():
    nodNo()
    time.sleep(3)

def destroy():
    servoSide.close()


if __name__ == "__main__":
    try:
        incorrect()
    except KeyboardInterrupt:
        destroy()