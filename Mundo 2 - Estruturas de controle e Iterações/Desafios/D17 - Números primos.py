# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

'''
if ( num % num ) == 0 and ( num % 1 ) == 0:
    print(' O número digitado é PRIMO')
else:
    print(' Infelizmente o número digitado NÃO É PRIMO')
'''
num = int(input('Digite um número inteiro: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[36m', end=' ') # Mostra os valores pelo qual ele o número é divisível
        tot += 1 # Realiza a contagem de quantas vezes foi divisivel
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m O número {} foi divisivel {} vezes'.format(num, tot))

if tot == 2: # Realiza a verificação se o número ' é ' ou ' não ' PRIMO!
    print('Por isso ele pe PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')
