"""
Crie um programa onde o usuário possa digitar '7 valores numéricos' e cadastre-os em uma 'lista única' que mantenha separados 
os valores 'pares' e 'impares'. No final mostre os valores pares e impares em ordem crescente.
"""
num = [[], []] # Lista simples dentro uma lista composta
valor = 0

for c in range(1, 8):
  valor = int(input(f'Digite o {c}º valor: '))
  # Par
  if valor % 2 == 0:
    num[0].append(valor) # Informando o indice da localização na lista composta
  # Impar
  else:
    num[1].append(valor) 

print('-=' * 20)
#print(f'Todos os valores: {num}')
# Organizando
num[0].sort()
num[1].sort()
print(f'Os valores pares são: {num[0]}')
print(f'Os valores impares são: {num[1]}')
print('-=' * 20)
