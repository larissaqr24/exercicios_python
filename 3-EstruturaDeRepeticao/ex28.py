'''Faça um programa que calcule o valor total investido por um colecionador
em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário
deverá informar a quantidade de CDs e o valor para em cada um.'''

qt_cds = int(input("Informe a quantidade de CDs: "))
soma = 0
for x in range(1, qt_cds+1):
    n = float(input("Informe o valor do {}º CD: ".format(x)))
    soma = soma + n


print("Valor total investido foi de R${}\n"
      "Valor médio gasto foi de R${}".format(soma, soma/qt_cds))
