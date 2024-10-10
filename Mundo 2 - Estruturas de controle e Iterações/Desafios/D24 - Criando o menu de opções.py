# Crie um programa que leia 2 valores e mostre um menu na tela:
"""
  [1] Somar
  [2] Multiplicar
  [3] Maior
  [4] Novos números
  [5] Sair do programa
"""
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import  sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

op = 0
maior = 0

while op != 5:

    print(''' 
    [ 1 ] Somar          
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    op = int(input('>>>>>> Qual a sua opção? '))

    if op == 1:
        s = n1 + n2
        print('A soma entre {} + {} = {}.'.format(n1, n2, s))
    elif op == 2:
        m = n1 * n2
        print('O resultado de {} x {} + {}.'.format(n1, n2, m))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os valores novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando....')
        sleep(2)
    else:
        print('Opçao inválida. Tente novamente!')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
