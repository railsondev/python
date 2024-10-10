# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual o preço do produto? R$ '))
de = int(input('Qual o desconto do produto? '))

d = (p * de)/100
np = p - d

print('O produto que custa {}, passará a custar {:.2f}, devido ao desconto de {}%.'.format(p, np, de))
