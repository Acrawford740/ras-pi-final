import playsound
import time

def noises():
    timesPlay = 0
    while timesPlay != 3:
        timesPlay += 1
        playsound('sound-effects/extremely-loud-incorrect-buzzer_0cDaG20.mp3')
        time.sleep(2)
        playsound('sound-effects/loud-correct-buzzer.mp3')
        time.sleep(2)

if __name == "__main__":
    try:
        noises()
    except KeyboardInterrupt:
        exit