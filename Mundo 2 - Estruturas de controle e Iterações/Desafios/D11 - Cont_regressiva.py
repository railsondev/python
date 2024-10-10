# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, 
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji

print('-=' * 2)
for c in range (10, -1, -1): # Começando do 10 a 0, voltando de 1 em 1
  print(c)
  sleep(0.5)
print(emoji.emojize('🎆🎆🎆🎆🎆🎆', language='pt'))
print('-=' * 2)
