# Escreva um programa que pergunte a quantidade de KM's percorridos por um carro alugado e a quantia de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por Km percorrido.

dias = int(input('Qunatos dias alugados? '))
km = float(input('Quantos KMs rodados? '))

v = (dias*60) + (km*0.15)

print('Olá, com a quantidade de {:.0f} dias e {:.0f} km percorridos, irá ser pago a quantia de R${:.2f}.'.format(
    dias, km, v))
