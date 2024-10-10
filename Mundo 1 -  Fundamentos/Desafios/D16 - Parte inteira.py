# Crie um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira.
# Digite um número:
# O número {} tem a parte inteira {}
'''from math import trunc

num = float(input('Digite um número com virgula: '))

print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))
'''

num = float(input('Digite um valor: '))

print('O valor digitado foi {} e a sua parte inteira é {}.'.format(
    num, int(num)))  # Utilizando a função interna 'int'
