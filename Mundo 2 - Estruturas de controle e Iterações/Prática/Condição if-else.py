nome = str(input('Qual o seu nome? '))

# Condição simples
if nome == 'Gustavo':
    print('Que nome bonito!')
# Condição composta aninhada
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claúdia Jéssica Juliana': # Realiza a filtro no nome digitado
    print('Belo nome feminino!')
else: # Opcional
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
