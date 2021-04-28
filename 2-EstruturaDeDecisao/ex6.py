'''Faça um Programa que leia três números e mostre o maior deles.'''

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = int(input("Informe o terceiro numero: "))

l = [n1, n2, n3]
l.sort()
print(l[2])

if n1 > n2:
    if n1 > n3:
        print(n1)
    else:
        print(n3)
else:
    if n2 > n3:
        print(n2)
    else:
        print(n3)