# Crie um programa que leia uma frase qualquer e diga se ela é um ' palindromo ', desconsiderando os espaços.

# EX: 
# APOS A SOPA 
# A SACADA DA CASA 
# A TORRE DA DERROTA 
# O LOBO AMA O BOLO 
# ANOTARAM A DATA DA MARATONA

'''
palavra = input('Digite uma frase: ').upper()

palavra_inv = palavra[::-1] # Realiza a leitura da palavra de trás para frente

if palavra == palavra_inv:
    print('A frase digitada é um PALÍNDROMO')
#print('O inversor da frase {} é {}'.format(palavra, palavra_inv))
'''

frase = input('Digite uma frase: ').strip().upper()

palavras = frase.split() # Separar em uma lista
junto = ''.join(palavras) # Juntar tudo em uma string só
inverso = ''

# Realizar o inverso da frase
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))

if inverso == junto:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É PALÍNDROMO!')
