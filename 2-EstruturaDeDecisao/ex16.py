'''Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e
fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''


a = int(input("Informe o valor de A: "))

if a == 0:
    print("A equação não pode ser realizada")
else:
    b = int(input("Informe o valor de B: "))
    c = int(input("Informe o valor de C: "))
    # delta = b² - 4ac
    delta = (b**2) - 4 * a * c
    print(delta)
    if delta < 0:
        print("Delta {} é negativo, a equação não possui raizes reais".format(delta))
    elif delta == 0:
        print("Delta igual a 0, a equação possui apenas uma raiz real")
    else:
        print("Delta é {}, a equação possui duas raiz reais".format(delta))
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print("x1 = {} e x2 = {}".format(x1, x2))
