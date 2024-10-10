# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for n in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(n)))
    if (num % 2) == 0:
        soma += num
        cont += 1
        
print('Você informou {} números PARES e a soma foi {}.'.format(cont, soma))
