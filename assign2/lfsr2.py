import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

musicFiles = []
usedValues = []

for i in range(20):
    musicFiles.append("./Audio/" + str(i+1) + ".mp3")

for dummy in range(20):
    d = random.randint(1, 20)
    while d in usedValues:
        d = random.randint(1, 20)
    usedValues.append(d)

for index in range(20):
    a = usedValues[index]
    pygame.mixer.music.load(musicFiles[a-1])
    pygame.mixer.music.play()

while True:
    arm = input()
    if arm == "next":
        pygame.mixer.music.stop()
        print("Music has been Stopped")
        d = (d + 1) % 20
        pygame.mixer.music.load(musicFiles[usedValues[d]-1])
        pygame.mixer.music.play()
        print(musicFiles[usedValues[d]-1] + "is playing")
    elif arm == "pause":
        pygame.mixer.music.pause()
    elif arm == "play":
        pygame.mixer.music.unpause()
        print("Music Resumed")
    elif arm == "quit":
        pygame.quit()
        sys.exit()

    elif not pygame.mixer.music.get_busy():
        print("Music has ended")
        index = (index + 1)%20
        a = usedValues[index]
        pygame.mixer.music.load(musicFiles[a-1])
        pygame.mixer.music.play()
        print(musicFiles[a-1])


