# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e a sua raiz quadrada.

print('Dobro | Triplo | Raiz quadrada \n')

n = int(input('Digite um número inteiro: '))

# d = n * 2
# t = n * 3
# rq = n **(1/2)

# print('O número digitado {} tem como \n Dobro {} \n Triplo {} \n Raiz quadrada {}'. format(n, d, t, rq))
print('O dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é igual a {:.2f}.'.format(
    n, (n*2), n, (n*3), n, pow(n, (1/2))))
