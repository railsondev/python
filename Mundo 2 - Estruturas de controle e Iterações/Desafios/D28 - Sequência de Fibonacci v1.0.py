# Escreva um programa que leia um número 'n' inteiro qualquer
# mostre na tela os 'n' primeiros elementos de uma sequência de Fibonacci.
'''
Ex:
  0 ->1 ->1 ->2 ->3 ->5 ->8
'''

print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)

n = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1

print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')

cont = 3

while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2  # Troca a posição
    t2 = t3  # Troca a posição
    cont += 1
print(' -> FIM!')
print('~' * 30)
