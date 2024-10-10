"""
pessoas = {'Nome':'Railson', 'Sexo':'M', 'Idade':30}
#del pessoas['Sexo']
pessoas['Nome'] = 'Leandro' # Trocando os valores da chave
pessoas['Peso'] = 98.5 # Incluindo um novo item no dicionário
#print(pessoas['Nome'])
#print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

for k in pessoas.keys():
  print(k)

for k in pessoas.values():
  print(k)

# Para utilizar o .items(), necessita-se de 2 identificadores  
for k, v in pessoas.items():
  print(f'{k} = {v}')

Brasil = []
estado1 = {'UF':'Rio de Janeiro', 'Sigla':'RJ'}
estado2 = {'UF':'São Paulo', 'Sigla':'SP'}

Brasil.append(estado1)
Brasil.append(estado2)

print(estado1)
print(estado2)
print(Brasil)
print(Brasil[0])
print(Brasil[1])
print(Brasil[0]['UF'])
print(Brasil[1]['Sigla'])
"""
Estado = dict()
Brasil = []

for c in range(0, 3):
    Estado
