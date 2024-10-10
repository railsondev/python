# Um professor quer sortear um dos seus alunos para apagar o quadro.
# Faça um programa que o ajude,lendo o nome deles e escrevendo o nome escolhido.
from random import choice

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]

print('Dentre os alunos, o escolhido foi: {}.'.format(
    choice(lista)))  # Retorna o escolhido dentre a lista
