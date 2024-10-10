"""
Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

Atualização:

Mostrar o tipo de triângulo formado:

Equilátero: Iguais
Isósceles: 2 iguais
Escaleno: Todos diferentes
"""

r1 = int(input('Qual o valor da primeira reta? '))
r2 = int(input('Qual o valor da segunda reta? '))
r3 = int(input('Qual o valor da terceira reta? '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possível sim construir um triângulo', end=' ')
    # Bloco de condicional aninhado
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1: # Realizando a verificação se o 1º é igual ao último
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Não será possivel construir um triângulo')
"""
if r1 == r2 == r3:
   print('O triângulo é EQUILÁTERO!')
elif r1 == r2 or r1 == r3 or r2 == r3:
   print('O triângulo é ISÓSCELES!')
elif r1 != r2 or r1 != r3:
    print('O triângulo é ESCALENO')
"""