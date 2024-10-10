"""
cont = 1

while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('ACABOU!')

# while True:
"""
"""
Realiza o loop  infinito

Para parar
    Apertar o botão STOP
    Utilizar o BREAK
"""
"""
n = s = 0
cont = 0

while True:  # Repetição utilizando flag que no caso é o 999
    n = int(input('Digite um número: '))
    # Parando o loop
    if n == 999:
        break
    s += n  # Realizando dos valores sem a flag
#print('A soma vale {}.'.format(s))

print(f'A soma vale {s}') # Uso da fstring que é chamada de interpolação dentro de strings
"""

n = 'José'
idade = 33
sal = 987.35

print(f'O {n} tem {idade} anos e ganha R${sal:.2f}')
