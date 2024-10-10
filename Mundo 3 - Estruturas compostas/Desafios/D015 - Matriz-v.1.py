"""
Crie um programa que crie uma 'matriz' de 'dimensão 3x3' e preencha com os valores lidos pelo teclado.
No final mostre a matriz da tela, com a formatação correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Alimenta a matriz
for l in range(0, 3):
  for c in range(0, 3): 
    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    
print('-=' * 30)
# Organizando a matriz
for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{matriz[l][c]:^5}]', end='') # O ':^5' serve para alinhar centralizado com a quantidade determinada
  print()
  