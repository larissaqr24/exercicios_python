'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''

l = []
par = []
impar = []

for x in range(20):
    l.append(int(input("Informe o {}º numero: ".format(x + 1))))

for x in l:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

print("Todos numeros: \n {}".format(l))
print("\nNumeros pares: \n {}".format(par))
print("\nNumeros impares: \n {}".format(impar))

