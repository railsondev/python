"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

Abaixo de 18.5: ABAIXO DO PESO
Entre 18.5 e 25: PESO IDEAL
25 até 30: SOBREPESO
30 até 40: OBESIDADE
Acima de 40: OBESIDADE MÓRBIDA
"""

h = float(input('Informe a sua altura: (m) '))
p = float(input('Informe o seu peso: (KG) '))

IMC = (p / h) /h

if IMC <= 18.5:
    print('Você está ABAIXO DO PESO, necessário se alimentar melhor.')
elif IMC >= 18.5 and IMC <= 25:
    print('Seu peso está IDEAL.')
elif IMC > 25 and IMC <= 30:
    print('Cuidado: Busque um médico, devido ao seu SOBREPESO.')
elif IMC > 30 and IMC <= 40:
    print('Atenção: Melhore a sua alimentação você já está no grau de OBESIDADE.')
elif IMC > 40:
    print('Deverá buscar um médico, pois já está em OBESIDADE MÓRBIDA.')
