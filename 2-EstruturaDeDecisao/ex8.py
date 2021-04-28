'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''


n1 = float(input("Informe o primeiro preço: "))
n2 = float(input("Informe o segundo preço: "))
n3 = float(input("Informe o terceiro preço: "))

l = [n1, n2, n3]
l.sort()
print(l[0])

if n1 < n2:
    if n1 < n3:
        print(n1)
    else:
        print(n3)
else:
    if n2 < n3:
        print(n2)
    else:
        print(n3)