from pygame import mixer
import time

def noises():
    timesPlay = 0
    while timesPlay != 3:
        timesPlay += 1
# Starting the mixer
        mixer.init()

# Loading the song
        mixer.music.load('/home/jack/CODE/ras-pi-final/sound-effects/loud-correct-buzzer.mp3')

# Setting the volume
        mixer.music.set_volume(0.7)

# Start playing the song
        mixer.music.play()
        time.sleep(2)

if __name__ == "__main__":
    try:
        noises()
    except KeyboardInterrupt:
        exit