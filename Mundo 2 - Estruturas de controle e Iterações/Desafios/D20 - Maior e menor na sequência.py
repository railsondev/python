# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o ' maior ' e ' menor ' peso lidos.

maior = 0
menor = 0

for p in range(1, 6):
  peso = float(input('Informe o {}º peso: '.format(p)))
  if p == 1: # Joga o 1º loop como maior e menor
    maior = peso
    menor = peso
  else:
    if peso > maior: # Verifica o peso maior
      maior = peso
    if peso < menor: # Verifica o menor peso 
      menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))
