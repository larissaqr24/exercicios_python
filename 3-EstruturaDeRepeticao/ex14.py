'''Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números impares.'''

list = []
par = impar = 0
for x in range(0, 10):
    list.append(int(input("Informe um numero inteiro: ")))

for x in list:
    if x % 2 == 0:
        par += 1
    else:
        impar += 1

print("Qtd de numeros pares: {}\n"
      "Qtd de numeros impares: {}".format(par, impar))
