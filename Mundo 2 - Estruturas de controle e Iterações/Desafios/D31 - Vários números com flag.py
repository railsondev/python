"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor '999', que é a 'Condição de parada'.
No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando a flag)
"""

quant = s = 0

while True:
    n = int(input('Digite um número inteiro: '))

    if n == 999:
        break

    quant += 1
    s += n
print(f'A quantidade de números foi {quant} e a soma dos valores é {s}')
