"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

(A) Quantos números foram digitados?
(B) A lista de valores, ordenada de forma decrescente.
(C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = list()

while True:
    
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar: [S/N] '))
    
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'A quantidade de valores na lista é: {len(lista)}')
lista.sort(reverse=True)
print(f'A lista decrescente é: {lista}')
if 5 in lista: # Busca dentro de uma coleção
    print('Foi localizado o valor 5 na lista')
else:
    print('O valor 5 não foi econtrado na lista')
print('-=' * 30)

"""
valores = []

quant = 0
resp = 'S'
valor = 5

while resp in 'Ss':

    valores.append(int(input('Digite um número: ')))
    #A
    quant += 1
    #B
    valores.sort(reverse=True) # Mostrando de tras para frente
    #C
    if valor in valores:
        print('O número 5 foi digitado')
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

print(f'A quantidade digitada foi: {quant}')
print(f'A lista decrescente é: {valores}')
"""