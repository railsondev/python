# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

print('Antecessor e Sucessor \n')

n = int(input('Digite o valor que deseja saber: '))

# a = n - 1
# s = n + 1

# print('O valor digitado {} tem como antecessor {} e sucessor {}'.format(n, a, s))
print('O número {}, tem como antecessor {} e sucessor {}'.format(n, (n-1), (n+1)))
