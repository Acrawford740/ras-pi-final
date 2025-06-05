import pygame
import time

# def load(song):
#     pygame.mixer.music.load("song")

def play():
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(.1)

pygame.init()
pygame.mixer.init()
load("/sound-effects/extremely-loud-incorrect-buzzer_0cDaG20.mp3")
play()