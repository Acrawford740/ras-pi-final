# ras-pie-final
Final Project For IOT Andrew/Jack

We are going to be making a program where you have to input a password and if you get it wrong a bobble head while shake it's head no and speakers or the buzzer will play an incorrect sound and if get the password correct the bobble head will shake it's head correct and it will play a correct sound.  We will connect a clock style 7 segment display and have buttons connected to it so if you push the top or bottom buttons it will change the number, but if you push the left or right buttons it will chage what number you are selected on.

needed items:
    Bobble Head
    Buzzer/Speakers
    Sound Effects
    7 Segment Clock Display
    Red & Yellow LEDs
    4 Buttons
    stepping motor
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
