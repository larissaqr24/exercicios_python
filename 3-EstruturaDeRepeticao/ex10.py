'''Faça um programa que receba dois números inteiros e gere os números
inteiros que estão no intervalo compreendido por eles.'''

n1 = int(input("Informe um numero: "))
n2 = int(input("Informe outro numero: "))

for x in range(n1+1, n2):
    print(x)