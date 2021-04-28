'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = int(input("Informe o terceiro numero: "))

l = [n1, n2, n3]
l.sort(reverse=True)
print(l)

