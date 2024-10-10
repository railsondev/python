"""
# num = (2, 5 ,9, 1) # Tupla
num = [2, 5, 9, 1]  # Lista
num[2] = 3  # Alterando o item
# num[4] = 7 # Inluindo um novo item da  forma errada
num.append(7) # Incluindo da forma correta
num.sort() # Organizando
num.sort(reverse=True) # Organizando de trás p/ frente
num.insert(2, 2) # Inserindo um novo item alterando os indices
#num.pop() # Removendo o último indices e junto o elemento
#num.pop(2) # Removendo o indice '2'
#num.remove(2) # Removendo o elemento solicitado
# Removendo utilizando o if
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4 solicitado')
print(num)
print(f'A lista possue {len(num)} elementos') # Trazendo a quantidade de elementos
"""

#valores = []
"""
valores.append(5)
valores.append(9)
valores.append(4)
"""
"""
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

#print(valores)
for c, v in enumerate(valores): # For a cada valor da lista trazendo o indice de cada valor
    print(f'Na posição {c} encontrei o valor {v}!')
print('\nCheguei ao final da lista')
"""
a = [2, 3, 4, 7]
b = a # Fazendo uma ligação entre as listas
b = a[:] # Fazendo a copia de uma lista na outra
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
