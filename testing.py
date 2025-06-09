from gpiozero import AngularServo
from time import sleep

GPIOside = 6
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
maxPW = (2.5 + myCorrection)/1000
minPW = (2.5 + myCorrection)/1000
servoUp = AngularServo(GPIOup, initial_angle=0, min_angle=0, max_angle=360, min_pulse_width = minPW, max_pulse_width = maxPW)

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

def incorrect():
    red_led.on()
    playsound('sound-effects/extremely-loud-incorrect-buzzer_0cDaG20.mp3')
    nodNo()
    time.sleep(3)
    red_led.off()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()