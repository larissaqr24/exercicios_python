'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

list = []
n = float(input("Informe uma nota. Para encerrar, digite 999: "))
c = 0
t = 0
while n != 999:
    if c == 0:
        list.append(n)
        c += 1
    else:
        n = float(input("Informe uma nota. Para encerrar, digite 999: "))
        list.append(n)

list.remove(999)
print("As notas informadas foram: {}\n"
      "A soma delas é: {}\n"
      "A média das notas é: {}".format(list, sum(list),
                                       sum(list) / len(list)))
