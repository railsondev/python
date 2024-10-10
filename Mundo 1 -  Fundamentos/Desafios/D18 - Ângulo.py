# Faça um programa que leia um ângulo e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

a = float(input('Digite o ângulo que desejas saber: '))

# O radians serve para converter o valor do ângulo em radiano
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))

print('O ângulo {}º tem o \n\nSENO de {:.2f} \nCOSSENO de {:.2f} \nTANGENTE de {:.2f}'.format(a, seno, cos, tan))
