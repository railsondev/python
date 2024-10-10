"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores inpares digitados, respectivamente.
No final, mostre o conteúdo das 3 listas geradas.
"""
num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um valor: ')))

    r = str(input('Deseja continuar: [S/N] '))

    if r in 'Nn':
        break
    
# Varrer verificando os pares oou impares
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista completa é {num}')
print(f'A lista dos valores pares é {pares}')
print(f'A lista dos valores impares é {impares}')

"""        
valores = []
par = []
impar = []

while True:

    valores.append(int(input('Digite um número: ')))

    if valores % 2 == 0:
        par = valores
    if valores % 2 != 0:
        impar = valores

    resp = str(input('Deseja incluir outro valor? [S/N] '))
    if resp in 'Nn':
        break
    

"""