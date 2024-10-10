"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:

Até 9 anos: MIRIM
Até 14 anos:INFANTIL
Até 19 anos:JÚNIOR
Até 20 anos:SÊNIOR
Acima:MASTER 
"""

from datetime import date

ano = int(input('Informe o ano de nascimento do atleta: '))

ano_atual = date.today().year

i = ano_atual - ano

print('O atleta tem {} anos.'.format(i))
if i <= 9:
    print('Categoria: MIRIM'. format(i))
elif i <= 14:
    print('Categoria: INFANTIL'. format(i))
elif i <= 19:
    print('Categoria: JÚNIOR'.format(i))
elif i <= 25:
    print('Categoria: SÊNIOR'.format(i))
else:
    print('Categoria: MASTER'.format(i))
