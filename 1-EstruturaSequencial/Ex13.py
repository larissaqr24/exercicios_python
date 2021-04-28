'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7
'''
altura = float(input("Informe sua altura: "))
peso_ideal_h = (72.7*altura) - 58
peso_ideal_m = (62.1*altura) - 44.7

print("Peso ideal para homem: " + str(peso_ideal_h))
print("Peso ideal para mulher: " + str(peso_ideal_m))
