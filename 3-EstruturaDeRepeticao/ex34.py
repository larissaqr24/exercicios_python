'''Os números primos possuem várias aplicações dentro da Computação, por
exemplo na Criptografia. Um número primo é aquele que é divisível apenas por
um e por ele mesmo. Faça um programa que peça um número inteiro e determine
se ele é ou não um número primo.'''

n = int(input("Informe um numero inteiro: "))
cont = 0
for x in range(1, n+1):
    if n % x == 0:
        cont += 1

if cont == 2:
    print("{} é primo!".format(x))
else:
    print("{} não é primo!".format(x))