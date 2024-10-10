# Faça um programa em python que abra e reproduza o aúdio de um arquivo MP3.

import pygame

# Inicializando o mixer PyGame
pygame.init()
# Carregar um arquivo de música para reprodução
pygame.mixer.music.load('audio.mp3')
# Iniciar a reprodução do fluxo de música
pygame.mixer.music.play()
input()
pygame.event.wait()
