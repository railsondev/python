# Desenvolva um programa que leia o ' primeiro termo ' e a ' razão ' de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

p = int(input('Primeiro elemento: '))
r = int(input('Razão: '))  # Os saltos realizados

decimo = p + (10 - 1) * r  # Formúla do Décimo termo de uma PA.

for t in range(p, decimo + r, r):
    print('{}'.format(t), end=' > ')
print('ACABOU!')
