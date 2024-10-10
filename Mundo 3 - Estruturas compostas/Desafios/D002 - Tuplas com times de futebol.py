"""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

[A] Apenas os 5 primeiros colocados
[B] Os últimos 4 colocados da tabela
[C] Uma lista com os times em ordem alfabética
[D] Em que posição na tabela está o time da 'Chapecoense'

"""
from operator import index
from os import times

tabela = ('Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo',
          'São Paulo', 'Cruzeiro', 'Atlético-MG','Red Bull Bragantino',
          'Palmeiras', 'Inter', 'Fortaleza', 'Grêmio', 'Vasco',
          'Criciúma', 'Juventude', 'Corinthians', 'Fluminense',
          'Vitória', 'Atlético-GO','Cuiabá')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 15)

# 5 primeiros colocados
print(f'Os 5 primeiiros colocados são: {tabela[0:5]}')
print('-=' * 15)

# Os últimos 4 colocados da tabela
print(f'Os últimos 4 colocados são: {tabela[-4:]}')
print('-=' * 15)

# Uma lista com os times em ordem alfabética
print(f'A tabela em ordem alfabética é: {sorted(tabela)}')
print('-=' * 15)

#[D] Em que posição na tabela está o time da 'Chapecoense'
print(f'A posição do São Paulo é: {tabela.index("São Paulo")+1}º')
print('-=' * 15)
'''
for t in tabela:
  print(t)
'''
