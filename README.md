# ras-pie-final
Final Project For IOT Andrew/Jack

We are going to be making a program where you have to input a password, and if you get it wrong a bobble head will shake its head no and speakers or the buzzer will play an incorrect sound. If you get the password correct, the bobblehead will shake its head correct and play a correct sound.  We will connect to GUIZero and have buttons in the GUI to type the password in.

needed items:
    Bobble Head
    Buzzer/Speakers
    Sound Effects
    Red & Green LEDs
    stepper motor
    2 220Ohm Resistors
    5 10KOhm Resistors

Connections:
    Left Button - GPIO24
    Top Button - GPIO25
    Right Button - GPIO23
    Bottom Button - GPIO27
    Red LED - GPIO26
    Yellow LED - GPIO4

Codeing Notes:
# Turn Off All The Segments
    for seg in segments.values():
        seg.off()

# 
