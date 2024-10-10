# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import choice, randint
from time import sleep

maq = randint(0,5) # Faz a máquina "PENSAR"

print('-=-' * 20)
print('Irei pensar em um número entre 0 e 5. Tente adivinhar .... ')
print('-=-' * 20)

user = int(input('Em qual número pensei? ')) # Jogador tenta adivinhar

print('PROCESSANDO....')
sleep(3) # Cria a simulação da máquina "PENSANDO"

if user == maq:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(maq, user))
