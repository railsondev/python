"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 KM/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por KM acima do limite.
"""

vel = float(input('Digite a velocidade do veiculo: '))

multa = (vel - 80) * 7

if vel > 80:
    print('Infelizmente você está acima da velocidade permitida')
    print('A sua será de R${:.2f}'.format(multa))
else:
    print('Você não será cobrado multa pode seguir normalmente')
