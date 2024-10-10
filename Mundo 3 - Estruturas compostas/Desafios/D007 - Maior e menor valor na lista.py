"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = []
maior = menor = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite o número {c}: '))) # Incluir valores em uma lista

    # Verificando o maior e menor valor
    if c == 0:
        maior = menor = valores[c]
    else:
       if valores[c] > maior:
           maior = valores[c]
       if valores[c] < menor:
           menor = valores[c]

print('-=' * 30)
print(f'Você digitou os números: {valores}')
print(f'O maior valor foi {maior} nas posições ', end='')
# Varrer uma lista
for i, v in enumerate(valores):
    if v  == maior:
        print(f'{i}...')
print(f'O menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...')
print('-=' * 30)
