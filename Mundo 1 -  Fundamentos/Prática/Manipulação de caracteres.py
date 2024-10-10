frase = 'Curso em Video Python'

#print(frase[::2])
#print(""" """) # Serve para exibir um bloco grande linhas
#print(frase.upper().count('O')) # Realizando a contagem da letra desejada sendo que a frase inteira for transformada para maiuscula
#print(len(frase.strip())) # Retorna o comprimento da frase removendo os espaços indesejads.
#print(frase.replace('Python','Android')) # Está trocando a palavra Python por Android
#print('Curso' in frase) # Está perguntando se na frase existe o nome 'Curso'
#print(frase.lower().find('video')) # Busca a palavra 'video' dentro da frase 'Curso em Video'
dividido = frase.split() # Transforma a frase em uma lista
#print(dividido[0]) # Retorna somente o item desejado conforme a sua numeração
print(dividido[2][3]) # Retorna o terceiro elemento do segundo elemento da lista