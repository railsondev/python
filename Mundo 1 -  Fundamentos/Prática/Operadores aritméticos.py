n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# O end= ' ' é utilizado para continuar na mesma linha, mesmo que a continuação esteja em outra linha.
# Para jogar a palavra para outra linha usa-se o \n
print('A soma é {}, o produto é {}, a divisão é {:.3f}'.format(s, m, d), end=' ') 
print('A divisão inteira é {} e a exponenciação {}'.format(di, e))
