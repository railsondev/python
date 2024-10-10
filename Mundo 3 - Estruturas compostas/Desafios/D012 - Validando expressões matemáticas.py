"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parêntese abertos e fechados na ordem correta.
"""

expr = str(input('Digite a expressão: '))
pilha = list()

# Busca o simbolo na lista
for simb in expr:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0: # Verifica a falta do último parênteses
      pilha.pop()
    else:
      pilha.append()
      break
if len(pilha) == 0:
  print('Sua expressão é válida!')
else:
  print('Sua expressão é inválida!')
