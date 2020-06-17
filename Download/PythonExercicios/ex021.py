#Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
import pygame
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()
#while pygame.mixer.music.get_busy():
    #pygame.time.Clock().tick(10)

#from pygame import mixer
#mixer.init()
#mixer.music.load('music.mp3')
#mixer.music.play()
#input('Agora você escuta?')
