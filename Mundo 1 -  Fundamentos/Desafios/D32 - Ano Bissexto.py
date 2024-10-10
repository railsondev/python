"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""
# Necessário que o resto da divisão da sua dezena do ano dividido por 4 seja igual a '0'.

ano = int(input('Digite um ano qualquer: '))

bis = (ano // 10 % 10) % 4 # Pega a dezena do ano e busca o resto da divisão por 4

if bis == 0: 
  print('O ano digitado {} é bissexto'.format(ano))
else:
  print('Infelizmente o {} digitado não é bissexto'.format(ano))
