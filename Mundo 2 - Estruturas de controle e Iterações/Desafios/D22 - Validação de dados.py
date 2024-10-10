# Faça um programa que leia o 'sexo', de uma pessoa, mas só aceite 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter o valor correto.

sexo = str(input(('Informe seu sexo [M/F]: '))).strip().upper()[0]

while sexo not in 'MmFf':
  sexo = str(input('Dados inválidos. Por,favor informe seus exo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
