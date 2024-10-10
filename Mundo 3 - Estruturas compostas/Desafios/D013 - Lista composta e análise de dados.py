"""
Faça um programa que leia o 'nome e o peso' de 'várias pessoas', guardando tudo em uma lista. No final, mostre:

[ A ] -> Quantas pessoas foram cadastradas?
[ B ] -> Uma listagem com as pessoas mais pesadas
[ C ] -> Uma listagem com as pessoas mais leves
"""
from ast import While


temp = []
princ = []
mai = men = 0

while True:

  temp.append(str(input('Nome: ')))
  temp.append(float(input('Peso: ')))
  #[B]
  if len(princ)  == 0:
    mai = men = temp[1]
  else:
    if temp[1] > mai:
      mai = temp[1]
    if temp[1] < men:
      men = temp[1]
  princ.append(temp[:]) # Evitando a repetição de informação
  temp.clear() 
  resp = str(input('Deseja continuar?[S/N] '))

  if resp in 'Nn':
    break

print('-=' * 30)
print(f'Os dados foram {princ}')
print(f'Ao todo foram cadastradas {len(princ)} pessoas.') # Utilizando o len() como contador
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
# Verificar menor
for p in princ:
  if p[1] == mai:
    print(f'[{p[0]}] ', end='')
print(f'O menor peso foi {men}Kg. Peso de ', end='')
# Verificar menor
for p in princ:
  if p[1] == men:
    print(f'[{p[0]}] ', end='')
print('-=' * 30)

"""
quant = totlev = totpes = 0
resp = 'S'
lista_geral = list()
lista_pes = list()
lista_lev = list()
dado = list()

while resp == 'S':

  dado.append(str(input('Nome: ')))
  dado.append(float(input('Peso: ')))
  lista_geral.append(dado[:])
  dado.clear()
  quant += 1
  
  resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
# [A]
print(f'A quantidade digitada foi {quant}')
# [B]
for p in lista_geral:
  if p[1] >= 100:
    lista_pes.append(lista_geral)
    quant += 1
    print(f'A lista de pessoas mais pesadas é {lista_pes}')
# [C]
for p in lista_geral:
  if p[1] <= 100:
    lista_lev.append(lista_geral)
    quant += 1
    print(f'A lista de pessoas mais leves é {lista_lev}')

# Lista uma abaixo da outra
for p in lista_geral:
  print(p)
"""
