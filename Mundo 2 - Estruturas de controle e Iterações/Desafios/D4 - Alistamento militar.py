"""
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade.

Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

ano = int(input('Qual o seu ano de nascimento: '))

ano_atual = date.today().year

alist = ano_atual - ano

#print('O ano atual é o {}'.format(ano_atual))
if alist < 18:
  print('Ainda não está no período de se alistar')
elif alist == 18:
  print('Está no ano de se alistar')
else:
  print('Infelizmente você já passou do peíodo de se alistar')
  