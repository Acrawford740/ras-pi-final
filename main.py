# Importing 
from guizero import App,TextBox,PushButton,Text, Picture
from gpiozero import LED, AngularServo
from pygame import mixer
import time

correctPass = "80085"

# Setting The LEDs
red_led = LED(23)
green_led = LED(18)

# Setting Servo Up
GPIOup = 5
SERVO_DELAY_SEC = 0.001
myCorrection = 0.0
maxPW = (2.5 + myCorrection)/1000
minPW = (2.5 + myCorrection)/1000
servoUp = AngularServo(GPIOup, initial_angle=0, min_angle=-180, max_angle=180, min_pulse_width = minPW, max_pulse_width = maxPW)

# Settign Servo Sideways
GPIOside = 6
servoSide = AngularServo(GPIOside, initial_angle=0, min_angle=-180, max_angle=180, min_pulse_width=minPW, max_pulse_width=maxPW)

def passwordCheck():
    if textEntry.value == correctPass:
        result.value = "Correct!"
        rightbuzz()
    else:
        result.value = "Incorrect!"
        wrongpic = Picture(app, image="images/FuedX-removebg-preview.png", height=70, width = 50)
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
        servoUp.angle = 10
        time.sleep(1)
        servoUp.angle = -80
        time.sleep(1)
    servoUp.angle = 5

def nodNo():
    timesNo = 0
    while timesNo != 5:
        timesNo += 1
        servoSide.angle = 40
        time.sleep(1)
        servoSide.angle = -40
        time.sleep(1)
    servoSide.angle = 0

# Close All
def destroy():
    red_led.close()
    green_led.close()
    servoUp.close()
    servoSide.close()
    
app = App(title = "Password Playtime!",width=300, height=200)

textEntry = TextBox(app, text="", hide_text=True)

checkButton = PushButton(app, text="Check Password", command=passwordCheck)

result = Text(app,text="")

app.display()