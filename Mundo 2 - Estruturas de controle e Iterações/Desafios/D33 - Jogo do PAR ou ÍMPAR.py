"""
Faça um programa que jogue 'par ou impar' com o computador.
O jogo só será interrompido quando o jogador 'PERDER', mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

v = 0

while True:
    jogador = int(input('Diga um valor: '))
    maq = randint(0, 11)
    tot = maq + jogador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0] # Para saber se a pessoa colocou par ou impar
    print(f'Você jogou {jogador} e o computador {maq}. Total de {tot} ', end='')
    print('DEU PAR' if tot % 2 == 0 else 'DEU IMPAR')

    if tipo == 'P':
        if tot % 2 == 0:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo  == 'I':
        if tot % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break

    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')