# Refaça o D51, lendo o ' primeiro termo ' e a ' razão ', de uma PA, 
# mostrando os 10 primeiros termos da PA usando a estrutura WHILE.

print('GERADOR DE PA')
print('-=' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

termo = p  # Mostra o termo
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r  # Atualizar o termo
    cont += 1

print('FIM!')
