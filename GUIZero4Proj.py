from guizero import App, Text, TextBox, PushButton

correctPass = "80085"

def passwordCheck():
    if textEntry.value == correctPass:
        result.value = "Correct!"
    else:
        result.value = "Incorrect!"

app = App(title = "Password Playtime!",width=300, height=200)

textEntry = TextBox(app, text="", hide_text=True)

checkButton = PushButton(app, text="Check Password", command=passwordCheck)

result = Text(app,text="")

app.display()