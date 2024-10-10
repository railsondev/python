"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

    O nome com todos maiusculas
    O nome com todas minusculas
    Quantas letras possue (sem considerar espaços)
    Quantas letras tem o primeiro nome
"""

nome = input('Digite o seu nome completo: ')

lista = nome.split()

print('A nome em maiusculo é {}.'.format(nome.upper()))
print('A nome em minusculo é {}.'.format(nome.lower()))
print('O seu nome tem {} caracteres.'.format(len(nome.strip())))
print('A primeira parte do seu nome tem {} caracteres.'.format(len(lista[0])))
