# Escreva um programa que leia um valor em metros e o exiba em centimetro e em milimetro.

n = float(input('Digite uma medida em metros: '))

km = n/1000
hm = n/100
dam = n/10
dm = n*10
c = n*100
mm = n*1000

print('A medida de {}m em \nKM é {}km \nHM é {}hm \nDAM é {}dam \nDM é {:.0f}dm \nCM é {:.0f}cm \nMM é {:.0f}mm \n '. format(
    n, km, hm, dam, dm, c, mm))
