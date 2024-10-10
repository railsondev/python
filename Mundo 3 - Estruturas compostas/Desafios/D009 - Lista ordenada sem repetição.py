"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem utilizar o sort()).

No final, mostre a lista ordenada na tela.
"""

lista = []

for v in range(0, 5):
    
    n = int(input(f'Digite o valor: '))
    
    # verificação da última posição
    if v == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        
        # Verificando a posição
        while pos < len(lista):
            if n <= lista[pos]:
                    lista.insert(pos, n)
                    print(f'Adicionado na posição {pos} da lista...')
                    break
            pos += 1
print('-=' * 30)
print(f"Lista atual: {lista}")
print('-=' * 30)

"""
    for i, v in enumerate(lista):
        if n < v:
            lista.insert(i, n)
            break
    else:
        lista.append(n)
"""