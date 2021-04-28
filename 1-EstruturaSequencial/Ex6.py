# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

r = int(input("Informe o raio do círculo: "))
a = math.pi * (r ** 2)
print("Área igual a: " + str(a))
