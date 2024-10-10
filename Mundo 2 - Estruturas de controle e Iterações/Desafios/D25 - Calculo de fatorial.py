# Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''
Ex:
  5! = 5x4x3x2x1 = 120
'''
from math import factorial

num = int(input('Digite um número inteiro para calcular o seu fatorial: '))
c = num

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' =', end='')
    #fat = factorial(num)
    c -= 1
#print('O fatorial de {} é {}.'.format(num, fat))
