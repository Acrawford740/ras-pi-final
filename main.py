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
servoUp = AngularServo(GPIOup, initial_angle=0, min_angle=0, max_angle=360, min_pulse_width = minPW, max_pulse_width = maxPW)

# Settign Servo Sideways
GPIOside = 6
servoSide = AngularServo(GPIOside, initial_angle=0, min_angle=0, max_angle=360, min_pulse_width=minPW, max_pulse_width=maxPW)

def passwordCheck():
    if textEntry.value == correctPass:
        result.value = "Correct!"
        rightbuzz()
    else:
        result.value = "Incorrect!"
        wrongpic = Picture(app, image="images/FuedX-removebg-preview.png", height=70, width = 50)
        wrongbuzz()

def wrongbuzz():
# Starting the mixer
        mixer.init()
# Loading the song
        mixer.music.load('/home/jack/CODE/ras-pi-final/sound-effects/incorrect_buzzer.mp3')

# Setting the volume
        mixer.music.set_volume(0.7)

# Start playing the song
        mixer.music.play()
        time.sleep(2)

def rightbuzz():
# Starting the mixer
        mixer.init()

# Loading the song
        mixer.music.load('/home/jack/CODE/ras-pi-final/sound-effects/loud-correct-buzzer.mp3')

# Setting the volume
        mixer.music.set_volume(0.7)

# Start playing the song
        mixer.music.play()
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

def correct():
    green_led.on()
    nodYes()
    time.sleep(3)
    green_led.off()

def incorrect():
    red_led.on()
    nodNo()
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
    
app = App(title = "Password Playtime!",width=300, height=200)

textEntry = TextBox(app, text="", hide_text=True)

checkButton = PushButton(app, text="Check Password", command=passwordCheck)

result = Text(app,text="")

app.display()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()
