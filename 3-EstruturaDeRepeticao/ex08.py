'''Faça um programa que leia 5 números e informe a soma e a média dos
números.'''

list = []
for x in range(0, 5):
    list.append(int(input("Informe um numero: ")))

print("Os numeros informados foram {}".format(list))
print("Soma é: {}".format(sum(list)))
print("A média é: {}".format(sum(list) / 5))
