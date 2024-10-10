"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu 'preço normal' e 'condição de pagamento'.

Á vista - dinheiro/cheque: 10% de desconto
Á vista - no cartão: 5% de desconto
Em até 2x no cartão: preço normal
3x ou + no cartão: 20% de juros
"""
print('{:=^40}'.format(' LOJAS GUANABARA '))
pn = float(input('Informe o valor do produto:R$ '))

print( ''' FORMAS DE PAGAMENTO:
[ 1 ] = Dinheiro | Cheque
[ 2 ] = Cartão
[ 3 ] = 2x no Cartão
[ 4 ] = 3x ou + no Cartão''')
op = input('Escolha uma opção de pagamento:')

if op == 1:
    nv = pn - (pn * 10 / 100)
    print('O valor a ser pago é {}'.format(nv))
elif op == 2:
    nv = pn - (pn * 5 / 100)
    print('O valor a ser pago é {}'.format(nv))
elif op == 3:
    print('O valor a ser pago é {}'.format(pn))
elif op == 4:
    j = pn + (pn * 20 / 100)
    tot_parc = int(input('Quantas parcelas? '))
    parc = pn / tot_parc
    print('Sua compra pacelada em {}x, será pago {}'.format(tot_parc, parc))
