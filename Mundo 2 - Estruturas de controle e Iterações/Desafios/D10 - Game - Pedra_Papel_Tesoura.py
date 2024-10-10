"""
Crie um programa que faça o computador jogar 'jokenpô' com você.
"""
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0,2) # Realiza o sorteio dos itens

print(''' Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')            
    elif jogador == 2:
        print('COMPUTADOR VENCE') 
    else:
        print('Jogada INVÁLIDA!')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VENCE')            
    elif jogador == 2:
        print('COMPUTADOR VENCE') 
    else:
        print('Jogada INVÁLIDA!')
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')            
    elif jogador == 2:
        print('COMPUTADOR VENCE') 
    else:
        print('Jogada INVÁLIDA!')