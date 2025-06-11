from pygame import mixer
from guizero import App,TextBox,PushButton,Text, Picture
import time
correctPass = "80085"

def passwordCheck():
    if textEntry.value == correctPass:
        result.value = "Correct!"
        rightpic.show()
        rightbuzz()
    else:
        wrongpic.show()
        result.value = "Incorrect!"
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

app = App(title = "Password Playtime!",width=300, height=200)

textEntry = TextBox(app, text="", hide_text=True)

checkButton = PushButton(app, text="Check Password", command=passwordCheck)

result = Text(app,text="")

rightpic = Picture(app, image="images/animations/Confetti.gif", height=100, width = 100)
wrongpic = Picture(app, image="images/FuedX-removebg-preview.png", height=70, width = 50)


wrongpic.hide()
rightpic.hide()
app.display()
