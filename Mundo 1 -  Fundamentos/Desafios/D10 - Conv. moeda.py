# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere
# US$1.00 = R$3.27

num = float(input('Informe o valor que possue em sua carteira: R$'))

d = num / 5.24
e = num / 5.56

print('Com o valor de R${:.2f} que possue hoje, poderá comprar U${:.2f} e E${:.2f}.'.format(
    num, d, e))
