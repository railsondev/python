"""
Crie um programa que leia um número e mostre na tela se ele é PAR ou IMPAR.
"""
num = int(input('Digite um número inteiro qualquer: '))

par = num % 2 # Retorna o resto da divisão

if par == 0: # Compara o resto com '0'
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))
