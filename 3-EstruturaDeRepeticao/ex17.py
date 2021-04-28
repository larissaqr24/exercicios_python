'''Faça um programa que calcule o fatorial de um número inteiro fornecido
pelo usuário. Ex.: 5!=5.4.3.2.1=120'''


def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1)


n = int(input("Informe um numero inteiro: "))

print(fatorial(n))

n_fat = 1
for x in range(1, n+1):
    n_fat = n_fat * x

print(n_fat)
