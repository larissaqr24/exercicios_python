'''Faça um programa que leia 5 números e informe o maior número.'''

list = []
for x in range(0, 5):
    list.append(int(input("Informe um numero: ")))

print("Os numeros informados foram {}".format(list))
list.sort(reverse=True)
print("O maior número é: {}".format(list[0]))
