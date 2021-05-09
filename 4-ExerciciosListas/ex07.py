'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma,
 a multiplicação e os números.'''

l = [10, 20, 30, 40, 50]


def soma_lista(lista):
    # metodo 1
    # r = 0
    # for x in lista:
    #     r = r + x

    # metodo 2
    r = sum(lista)

    return r


def mult_lista(lista):
    import math
    # metodo 1
    # r = 1
    # for x in lista:
    #     r = x * r

    # metodo 2
    r = math.prod(lista)

    return r


print(soma_lista(l))
print(mult_lista(l))
