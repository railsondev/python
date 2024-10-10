# Crie um programa que mostre na tela todos os números pares que estão entre 1 e 50.

# Fazendo mais iterações
'''
for c in range(1, 51):
    if (c % 2) == 0:
        print(c, end=' ')
'''

# Economizando esforço
for c in range(2, 51, 2): # Começando do 2, executando um salto de de 2 em 2.
    print(c, end=' ')
print('ACABOU!')
