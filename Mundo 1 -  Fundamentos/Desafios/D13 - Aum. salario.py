# Faça um algoritimo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.

s = float(input('Qual o seu salário?R$ '))
ds = int(input('Qual a porcentagem do aumento do salário? '))

a = (s*ds)/100
ns = s + a

print('O salário R${:.3f} de hoje, com o aumento de {}%, passará a ser de R${:.4f}.'.format(s, ds, ns))
