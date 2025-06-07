from guizero import App, Text, TextBox, PushButton
from playsound import playsound
correctPass = "80085"

def passwordCheck():
    if textEntry.value == correctPass:
        result.value = "Correct!"
        playsound('.\sound-effects\loud-correct-buzzer.mp3')
    else:
        result.value = "Incorrect!"
        playsound('sound-effects/extremely-loud-incorrect-buzzer_0cDaG20.mp3')

app = App(title = "Password Playtime!",width=300, height=200)

textEntry = TextBox(app, text="", hide_text=True)

checkButton = PushButton(app, text="Check Password", command=passwordCheck)

result = Text(app,text="")

app.display()