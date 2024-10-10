# Refaça o D009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('-=' * 14)
tab = int(input('Qual o número da tabuada? '))
print('-=' * 14)

for t in range(0 , 11, +1): # Em uma crescente sempre acrescente um número ao final, ou seja , se o final é '10' coloque '11'.
    print('{} x {:2} = {} '.format(tab, t, tab*t))

print('-=' * 14)
