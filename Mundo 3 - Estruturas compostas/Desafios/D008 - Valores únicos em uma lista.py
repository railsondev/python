"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
lista = list()

while True:

    n = int(input('Digite um valor: '))
    
    # Verificação na lista
    if n not in lista: # Verifica se existe na lista
        lista.append(n)
        print('Realizado a inserção com sucesso!!!')
    else:
        print('Valor duplicado!!!')
    
    r = str(input('Deseja continuar:[S/N] '))
    
    if r in 'Nn':
        break

print('-=' * 30)
lista.sort()
print(f'Os valores digitados foram: {lista}')
print('-=' * 30)
