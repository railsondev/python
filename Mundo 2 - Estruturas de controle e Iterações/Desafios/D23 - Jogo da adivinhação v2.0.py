# Melhore o jogo do D28, onde o computador vai ' pensar ', em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram neccessários para vencer.

from random import randint

maq = randint(0, 10)

print('Sou seu computador ... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

acertou = False
tent = 0
while not acertou: # Enquanto não acertar
# Obs: Sai do loop quando o não for 'True'
  jogador = int(input('Qual o seu palpite? '))
  tent += 1 # Contador de tentativas
  if jogador == maq:
    acertou = True # Testa se já acertou
  else:
    if jogador < maq: # Verificação se passou ou não
      print('Mais... Tente mais uma vez!')
    elif jogador > maq:
      print('Menos... Tente mais uma vez!')

print('Acertou com {} tentativas! PARABÉNS!'.format(tent))
