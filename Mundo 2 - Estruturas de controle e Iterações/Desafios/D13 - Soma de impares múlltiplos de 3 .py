# Faça um progrma que calcule a soma entre todos os números impares que são múltiplos de 3 e que se encontram no intervalo entre 1 até 500.

'''
for i in range(1, 501, +1):
    if (i % 3) == 0:
        if (i % 2) != 0:
            print(i, end=' ')
'''
soma = 0
cont = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        # print(i, end=' ') # Listagem
        cont += 1 # Realizando a contagem
        soma += i # Realizando o acumulamento
        
print(f'A soma de todos os {cont} valores solicitados é {soma}')
