"""
Crie um programa de 'nome' e o 'preço' de 'várias pessoas'.
O programa deverá perguntar se o 'usuário' vai continuar.
No final, mostre:

[A] Qual é o total gasto na compra?
[B] Quantos produtos custam mais de R$ 1000
[C] Qual é o nome do produto mais barato?
"""
tot = tot_mil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço:R$ '))

    cont += 1
    # Letra A
    tot += valor
    # Letra B
    if valor > 1000:
        tot_mil += 1
    # Letra C
    # Verificação do menor
    if cont == 1 or valor < menor: # Simplificando o código
        menor = valor
        barato = produto
    """
    else:
        if valor < menor:
            menor = valor
            barato = produto
    """
    # Possibilita o True do While
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA')) # Realiza a centralização do texto em tantos espaços
print(f'O total da compra foi R$ {tot:.2f}')
print(f'Temos {tot_mil} produtos custando mais de R$ 1.000.00.')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
