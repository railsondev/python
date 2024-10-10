"""
Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
r1 = int(input('Qual o valor da primeira reta? '))
r2 = int(input('Qual o valor da segunda reta? '))
r3 = int(input('Qual o valor da terceira reta? '))

if r1+r2>r3 or r2+r3>r1 or r1+r3>r2:
  print('É possível sim construir um triângulo')
else:
  print('Não será possivel construir um triângulo')
