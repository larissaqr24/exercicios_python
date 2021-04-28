'''Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo
e por 1.'''

n = int(input("Informe um numero inteiro: "))
cont = 0
for x in range(1, n+1):
    if n % x == 0:
        cont += 1

if cont == 2:
    print("{} é primo!".format(x))
else:
    print("{} não é primo!".format(x))
