"""
Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço, cobrando R$0,50 por KM para viagens de até 200 KM e R$0,45 para viagens mais longas.
"""
dis = float(input('Informe a distância da viagem: KM '))

a = dis * 0.50
l = dis * 0.45

if dis <= 200:
    print('O valor a ser cobrado será de {}'.format(a))
else:
    print('O valor a ser cobrado será de R${:.2f}'.format(l))
