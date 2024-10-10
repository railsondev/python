"""
Faça um programa que leia 3 números e mostre qual é o menor.
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

menor = n1

if menor < n2 and menor < n3:
  print('O menor número é {}'.format(menor))
elif n2 < menor and n2 < n3:
  print('O menor número é {}'.format(n2))
else:
  print('O menor número é {}'.format(n3))
