"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

[A] Quantas vezes apareceu o valor '9'?
[B] Em que posição foi digitado o primeiro 3?
[C] Quais foram os números pares?

"""
# Guardando os valores em uma tupla
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'Você digitou os valores: {num}')

# A
print(f'O valor 9 apareceu {num.count(9)} vezes.') # Fazendo a verificação especifica dentro da tupla


# B
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
# C
print('Os valores pares digitados foram: ', end='')

for n in num:
    if n % 2 == 0:
        print(n, end='  ')
