"""
teste = list()

teste.append('Gustavo')
teste.append(40)

galera = list()
# galera.append(teste) # Fazendo alteração em ambas as listas
galera.append(teste[:]) # Mostrando o valor verdadeiro da lista
teste[0] = 'Maria'
teste[1] = 22

# galera.append(teste) # Fazendo alteração em ambas as listas
galera.append(teste[:]) # Mostrando o valor verdadeiro da lista
print(galera)

# Inclusão direto na lc

galera =[['Railson', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] # Lista composta
# print(galera[2][1])
for p in galera:
  #print(p) # Mostra as listas simples uma abaixo da outra
  #print(p[1]) # Mostra somente os elementos do indice 0 da lista simples
  print(f'{p[0]} tem {p[1]} anos de idade')
"""

# Verificação temporária

galera = list()
dado = list()
totmai = totmen = 0 

# Inclusão e exclusão dos dados
for c in range(0, 3):
  dado.append(str(input('Nome: ')))
  dado.append(int(input('Idade: ')))
  galera.append(dado[:])
  dado.clear()
  
# Verificação dos dados
for p in galera:
  if p[1] >= 21:
    print(f'{p[0]} é maior de idade.')
    totmai += 1
  else:
    print(f'{p[0]} é menor de idade.')
    totmen += 1
    
print(f'Temos {totmai} pessoas maiores de idade e {totmen} menores de idade.')
