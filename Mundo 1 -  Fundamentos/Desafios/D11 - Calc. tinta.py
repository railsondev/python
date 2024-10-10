# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a área e a quantidade de tinta necessária para pintá-la.
# Considere
# 1ltinta == 2 m²

l = float(input('Qual a largura da parede em m? '))
h = float(input('Qual a altura da parede em m? '))

a = l * h
t = a / 2

print('A sua parede tem a dimensão de {} x {} e a sua área é de {}m².'.format(l, h, a))
print('Para pintar a parede, necessita-se de {}l de tinta'.format(t))
