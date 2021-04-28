'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da
tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
de latas de tinta a serem compradas e o preço total.
'''


v_metro2 = float(input("Informar tamanho a ser pintado em metros quadrados: "))
vl_cobertura = 3
v_lata = 18
vl_tinta = 80

vl_litros_necessario = v_metro2 / vl_cobertura

if vl_litros_necessario <= v_lata:
    print("Voce precisa de 1 lata. O valor total é de R$" + str(vl_tinta))
else:
    qtd_lata = round(vl_litros_necessario / v_lata)
    vl_total = qtd_lata * vl_tinta
    print("Voce precisa de " + str(qtd_lata) + " lata. O valor total é de R$" + str(vl_total))
