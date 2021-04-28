'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''

n1 = int(input("Informe 1º numero inteiro: "))
n2 = int(input("Informe 2º numero inteiro: "))
n3 = float(input("Informe um numero real: "))

r1 = (n1*2) * (n2/2)
r2 = (n1*3) + n3
r3 = n3 ** 3

print(r1)
print(r2)
print(r3)
