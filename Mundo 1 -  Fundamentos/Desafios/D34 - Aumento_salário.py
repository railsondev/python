"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%
"""
sal = float(input('Qual o seu salário?R$ '))

if sal > 1.250:
  aum_s = sal + ((sal * 10) / 100)
  print('Com o aumento de 10%, passará a receber {:.3f}'.format(aum_s))
else:
  aum_i = sal + ((sal * 15) / 100)
  print('Com o aumento de 15%, passará a receber {:.3f}'.format(aum_i))
