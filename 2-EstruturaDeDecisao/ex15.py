'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem
um triângulo, se o mesmo é: equilátero, isósceles ou escaleno
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for
maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''


def eh_triangulo(l1, l2, l3):
    if (l1 + l2) > l3:
        return True
    elif (l2 + l3) > l1:
        return True
    elif (l3 + l1) > l2:
        return True
    else:
        return False


def tp_triangulo(l1, l2, l3):
    if l1 == l2 and l2 == l3:
        print("Triângulo Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo Isósceles")
    elif l1 != l2 and l2 != l3:
        print("Triângulo Escaleno")
    else:
        print("Não idenficado")


l1 = float(input("Informe o primeiro lado do triângulo: "))
l2 = float(input("Informe o segundo lado do triângulo: "))
l3 = float(input("Informe o terceiro lado do triângulo: "))

if eh_triangulo(l1, l2, l3):
    tp_triangulo(l1, l2, l3)
else:
    print("Não é triângulo")
