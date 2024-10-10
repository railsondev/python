
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
"""
# Tuplas são imutáveis
# lanche[1] = 'Refrigerante' -> Errado
"""
# print(len(lanche))
for comida in lanche: # Sem a necessidade da posição
    print(f'Eu vou comer {comida}')
"""
# Precisando da posição
for pos, comida in enumerate(lanche):  # Utilizando a varíavel
  print(f'Eu vou comer {comida} na posição {pos}')
  
for cont in range(0, len(lanche)):  # Utilizando o range
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

print(sorted(lanche)) # Organizar em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)

c = a + b

print(c)
print(c.count(5)) # Realiza a busca dentro da varíavel e construção é variável.cont(x)
print(c.index(2, 1)) # Retorna a posição do parâmetro, utilizando o deslocamento

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # Exclui a varíavel
print(pessoa)
"""