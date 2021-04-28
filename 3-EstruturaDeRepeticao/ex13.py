'''Faça um programa que peça dois números, base e expoente, calcule e mostre
 o primeiro número elevado ao segundo número. Não utilize a função de
 potência da linguagem.'''

base = int(input("Informe um numero base: "))
expo = int(input("Informe um numero expoente: "))
result = base
for x in range(1, expo):
    result = result * base

print(result)
