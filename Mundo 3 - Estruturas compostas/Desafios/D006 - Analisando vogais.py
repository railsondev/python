"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

# Analise os elementos da tupla
for p in palavras:
  print(f'\nNa palavra {p.upper()} temos: ', end='')
  # Pegar cada letra
  for letra in p: 
      # Analisar separado
      if letra.lower() in 'aeiou':
        print(letra, end=' ')
        