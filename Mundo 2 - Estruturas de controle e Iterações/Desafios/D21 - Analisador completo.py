# Desenvolva um programa que leia o ' nome ',' idade ' e ' sexo ' de ' 4 pessoas '. 
# No final do programa, mostre: 
# A média de idade do grupo 
# Qual é o nome do homem mais velho 
# Quantas mulheres tem menos de 20 anos.

soma_id = 0
média_id = 0
maior_id_h = 0
nome_v = ''
tot_mul_20 = 0

for p in range(1, 5):
  print('------- {}º pessoa --------'.format(p))
  nome = str(input('Nome: ')).strip()
  idade = int(input('Idade: '))
  Sexo = str(input('[M/F]: ')).strip()
  
  soma_id += idade
  
  # Verificação do homem + velho
  if p == 1 and Sexo in 'Mm':
    maior_id_h = idade
    nome_v = nome
  if Sexo in 'Mm' and idade > maior_id_h:
    maior_id_h = idade
    nome_v = nome
  
  # Verificação da quant. de mulheres < 20 anos
  if Sexo in 'Ff' and idade < 20:
    tot_mul_20 += 1
    
média_id = soma_id / 4

print('A média de idade do grupo é {} anos.'.format(média_id))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_id_h, nome_v))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(tot_mul_20))
