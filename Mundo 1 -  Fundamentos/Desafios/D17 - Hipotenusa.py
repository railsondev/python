# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# from math import hypot
'''
from math import sqrt

ca = int(input('Cateto adjacente: '))
co = int(input('Cateto oposto: '))

hip = sqrt(ca*ca + co*co)

# print('O cateto adjecente {} e cateto oposto {} tem como hipotenusa {:.2f}.'.format(ca, co, hypot(ca, co)))
print('O cateto adjacente {} e o cateto oposto {} tem como hipotenusa {:.2f}.'.format(ca, co, hip))
'''
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

hi = (ca ** 2 + co ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}.'.format(hi))
