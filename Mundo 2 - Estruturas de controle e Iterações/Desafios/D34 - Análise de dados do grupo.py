"""
Crie um programa que leia a 'idade' e o 'sexo' de 'várias pessoas'.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final mostre:

[A] Quantas pessoas tem mais de 18 anos?
[B] Quantos homens foram cadastrados?
[C] Quantas mulheres tem menos de 20 anos?
"""
tot18 = tot_h = tot_m20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': # Impossibilita de outra letra
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0] # Pegar a 1º letra

    if idade >= 18:
        tot18 += 1

    if sexo == 'M':
        tot_h += 1

    if sexo == 'F' and idade < 20:
        tot_m20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'A quantidade de pessoas com mais de 18 anos são: {tot18}')
print(f'Ao todo temos {tot_h} homens cadastrados.')
print(f'Ao todo temos {tot_m20} mulheres com menos de 20 anos.')
