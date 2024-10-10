"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
O programa vai perguntar o valor da casa,o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode execeder 30% do salário ou então o emprétimo será negado.
"""

sal = float(input('Informe o valor do seu salário:R$ '))
casa = float(input('Qual o valor da casa?R$ '))
anos = int(input('Quantos anos desejas pagar a casa? '))

lim_sal = sal * 30 / 100
p_casa = casa / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'. format(casa, anos, p_casa))

if p_casa < lim_sal:
  print('Será concedido o empréstimo para a compra da casa')
else:  
  print('Infelizmente não será possível a concessão do emprestimo')
