'''Faça um Programa que peça dois números e imprima o maior deles.'''
n1 = int(input("Informe um numero: "))
n2 = int(input("Informe outro numero: "))

if n1 == n2:
    print("Os dois numeros são iguais")
elif n1 > n2:
    print(n1)
else:
    print(n2)