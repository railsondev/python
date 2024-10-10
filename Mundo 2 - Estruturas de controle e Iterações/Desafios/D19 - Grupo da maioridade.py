# Crie um programa que leia o ' ano de nascimento ' de ' 7 pessoas '. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores.

from datetime import date

ano_atual = date.today().year

cont = 0
cont_menor = 0

for m in range(1, 8):
  nasc = int(input('Informe o {}º ano de nascimento: '.format(m)))
  if (ano_atual - nasc) >= 18:
    cont += 1
  else:
    cont_menor += 1
    
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont))
print('E tivemos {} pessoas menores de idade'.format(cont_menor))
