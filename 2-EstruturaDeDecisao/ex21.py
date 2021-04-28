'''Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três
notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e
quatro notas de 1.'''


saque = int(input("Informe o valor do saque: "))
notas = [100, 50, 10, 5, 1]
nota_100 = 0
nota_50 = 0
nota_10 = 0
nota_5 = 0
nota_1 = 0
rest = saque
if saque in range(9, 601):
    while rest > 0:
        if rest >= notas[0]:
            nota_100+=1
            rest = rest - 100
        elif rest >= notas[1]:
            nota_50+=1
            rest = rest - 50
        elif rest >= notas[2]:
            nota_10 += 1
            rest = rest - 10
        elif rest >= notas[3]:
            nota_5+=1
            rest = rest - 5
        elif rest >= notas[4]:
            nota_1+=1
            rest = rest - 1

    print("Para sacar a quantia de {}, precisa de {} notas de 100, {} notas de 50, {} notas de 10, {} notas de 5 e {} notas de 1.".format(saque, nota_100, nota_50, nota_10, nota_5, nota_1))
else:
    print("Informar um valor entre R$10 a R$600")