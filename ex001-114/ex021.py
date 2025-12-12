import pygame, sys
from pygame import mixer

pygame.init()

mixer.music.load('Olivia Rodrigo - good 4 u (Official Video).mp3')

def playSound():
    while True:
        userInput = input('')

        if userInput == 'p':
            mixer.music.play()
        if userInput == 'q':
            mixer.music.pause()
        if userInput == 'b':
            break
playSound()