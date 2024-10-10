"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

Ex:

    Ana Maria de Souza
    Primeiro: Ana
    Último: Souza
"""
n = str(input('Digite o seu nome completo: ')).strip()

nome = n.split() # Fatiar a palavra

print('Olá, muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('O seu último nome é {}'.format(nome[len(nome)-1])) # Pega o comprimento do nome e subtrai 1, mostrando o último item da lista
