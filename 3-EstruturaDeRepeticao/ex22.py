'''Altere o programa de cálculo dos números primos, informando, caso o número
não seja primo, por quais número ele é divisível.'''

n = int(input("Informe um numero inteiro: "))
cont = 0
list = []
for x in range(1, n+1):
    if n % x == 0:
        cont += 1
        list.append(x)

if cont == 2:
    print("{} é primo!".format(x))
else:
    print("{} não é primo!"
          "Ele é divisivel por {}".format(x, list))

