"""
Faça um programa que mostre a tabuada de vários números um de cada vez, para cada valor digitado pelo usuário.
O programa será 'interrompido' quando o número solicitado for 'negativo'.
"""

while True:
    print('-=' * 18)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-=' * 18)

    if n < 0:
        break

    for t in range(0, 11):
        print(f'{n} x {t} = {n*t}')

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
