'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de
R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável
multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
'''
limite = 50
multa_kilo = 4

peso_peixe = float(input("Informe o peso do peixe: "))

excesso_kilo = peso_peixe - limite

if excesso_kilo > 0:
    multa = excesso_kilo * multa_kilo
    print("Seu peixe excedeu " + str(excesso_kilo) + " kilos.")
    print("O valor da multa é: R$" + str(multa) + ".")
else:
    print("Seu peixe está dentro do limite.")

