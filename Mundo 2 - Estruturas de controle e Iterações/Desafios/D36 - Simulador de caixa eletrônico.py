"""
Crie um programa que simule o funcionamento de um 'caixa eletrônico'.
No início, pergunte ao usuário qual será oo valor sacado(nº inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs:

    Considere que o caixa possui cédulas de R$50, R$29, R$19 e R$1.
"""

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Digite o valor inteiro que desejas sacar: R$ '))
total = valor
ced = 50
tot_ced = 0

while True:

    if total >= ced:
        total -= ced
        tot_ced += 1
    else:
        if tot_ced:
            print(f'Total de {tot_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot_ced = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CURSO EM VIDEO! tenha um bom dia')
