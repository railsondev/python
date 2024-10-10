# Melhore o D61, perguntando para o usuário se ele quer mostrar alguns termos. 
# O programa encerrar quando ele disser que quer mostrar 0 termos.

print('GERADOR DE PA')
print('-=' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

termo = p  # Mostra o termo
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais # Contador dos termos exibidos na tela
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r  # Atualizar o termo
        cont += 1

    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
