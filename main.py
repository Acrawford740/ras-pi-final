# Importing 
from guizero import App,TextBox,PushButton,Text, Picture
from gpiozero import LED, AngularServo
import os
from pygame import mixer
import time
os.environ["GPIOZERO_PIN_FACTORY"] = 'pigpio'

correctPass = "80085"

# Setting The LEDs
red_led = LED(23)
green_led = LED(18)



# Setting Servo Up
GPIOup = 5
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
minPW = 0.0006
maxPW = 0.0024
servoUp = AngularServo(GPIOup, initial_angle=-60, min_angle=-180, max_angle=180, min_pulse_width = minPW, max_pulse_width = maxPW)

# Settign Servo Sideways
GPIOside = 6
servoSide = AngularServo(GPIOside, initial_angle=-30, min_angle=-180, max_angle=180, min_pulse_width=minPW, max_pulse_width=maxPW)

def passwordCheck():
    if textEntry.value == correctPass:
        result.value = "Correct!"
        wrongpic.hide()
        rightpic.show()
        rightbuzz()
    else:
        result.value = "Incorrect!"
        rightpic.hide()
        wrongpic.show()
        wrongbuzz()

def wrongbuzz():
# Play The Incorrect Sound Effect
    mixer.init()
    mixer.music.load('/home/jack/CODE/ras-pi-final/sound-effects/incorrect_buzzer.mp3')
    mixer.music.set_volume(0.7)
    red_led.on()
    mixer.music.play()
    # Makes The Bobble Head Nod No
    nodNo()
    red_led.off()
    time.sleep(2)


def rightbuzz():
# Play The Correct Sound Effect
    mixer.init()
    mixer.music.load('/home/jack/CODE/ras-pi-final/sound-effects/loud-correct-buzzer.mp3')
    green_led.on()
    mixer.music.play()
    nodYes()
    green_led.off()
    time.sleep(2)

def nodYes():
    timesYes = 0
    while timesYes != 5:
        timesYes += 1
        servoUp.angle = 0
        time.sleep(1)
        servoUp.angle = -80
        time.sleep(1)
    servoUp.angle = -60

def nodNo():
    timesNo = 0
    while timesNo != 5:
        timesNo += 1
        servoSide.angle = 20
        time.sleep(.5)
        servoSide.angle = -60
    time.sleep(.5)
    servoSide.angle = -30

# Close Allresult = Text(app,text="")

    
app = App(title = "Password Playtime!",width=300, height=200)

textEntry = TextBox(app, text="", hide_text=True)

checkButton = PushButton(app, text="Check Password", command=passwordCheck)

result = Text(app,text="")

rightpic = Picture(app, image="images/animations/Confetti.gif", height=100, width = 100)
wrongpic = Picture(app, image="images/FuedX-removebg-preview.png", height=70, width = 50)

wrongpic.hide()
rightpic.hide()
app.display()