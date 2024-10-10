"""
Escreva um programa que leia 2 números inteiros e compare-os, mostrando na tela uma mensagem:

O primeiro valor é o maior
O segundo valor é o maior
Não existe valor maior, os dois são iguais
"""
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))

if n1 > n2:
  print('O valor {} é o maior.'.format(n1))
elif n1 < n2:
  print('O valor {} é o maior.'.format(n2))
else:
  print('Os valores digitados são iguais.'.format(n1, n2))
