"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

1 para binário
2 para octal
3 para hexadecimal
"""

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
      [1] Converter para BINÁRIO
      [2] Converter para OCTAL
      [3] Converter para HEXADECIMAL''')

op = int(input('Sua opção: '))

if op == 1:
  print('{} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:])) # O [2:] serve para remover os 2 elementos mostrados
elif op == 2:
  print('{} convertido para OCTAL é {}.'.format(num, oct(num)[2:]))
elif op == 3:
  print('{} convertido para HEXADECIMAL é {}.'.format(num, hex(num) [2:]))
else:
  print('Opção inválida. Tente novamente.')
