# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input("Digite algo: ")

print("====================================================")
print("================ Análise da palavra ================")
print("O tipo primtivo desse valor é: ", type(a))
print("Só  tem espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanúmerico? ", a.isalnum())
print("Está em maiuscula? ", a.isupper())
print("Éstá em minúscula?  ", a.islower())
print("Éstá capitalizada? ", a.istitle())
print("====================================================")
