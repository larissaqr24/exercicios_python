'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os
valores para cima, isto é, considere latas cheias.
'''
import math

v_area = float(input("Informar tamanho a ser pintado em metros quadrados: "))
vl_cobertura = 6
v_lata = 18
vl_lata = 80
v_galao = 3.6
vl_galao = 25

v_litros = v_area / vl_cobertura
v_litrosf = math.ceil(float(v_litros*1.1))

if v_litrosf <= v_galao:
    print("Voce precisa de 1 galão. O valor total é de R${}".format(vl_galao))
elif v_litrosf <= v_lata:
    print("Voce precisa de 1 lata. O valor total é de R${}".format(vl_lata))
else:
    vl_litros_lata = math.ceil(float(v_litrosf) / v_lata)
    print(vl_litros_lata)
    vl_litros_galao = math.ceil(float(v_litrosf) / float(v_galao))
    print(vl_litros_galao)
    v_preco_lata = vl_litros_lata * vl_lata
    print(v_preco_lata)
    v_preco_galao = vl_litros_galao * vl_galao
    print(v_preco_galao)
    qtd_lata = int(v_litrosf / v_lata)
    rest = v_litrosf % v_lata
    print(rest)
    qtd_galao = math.ceil(rest / v_galao)
    valor = ((qtd_lata * 80) + (qtd_galao * 25))
    print('Você irá precisar de {} latas, {} galões no valor de R${}.'.format(qtd_lata, qtd_galao, valor))
