"""
Crie um programa que leia 2 notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
"""

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

m = (n1+n2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if m < 5.0:
    print('Infelizmente você ficou REPROVADO!')
elif 7 > m >= 5.0:
    print('Você ficou de REPOSIÇÃO')
elif m >= 7.0:
    print('PARABÉNS! Você foi APROVADO!')
