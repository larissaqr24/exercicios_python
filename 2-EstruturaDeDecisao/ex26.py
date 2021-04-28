'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o
número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o
preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''


litros = float(input("Informe a quantidade de litros: "))
comb = input("Informe o tipo de combustivel \n "
             "A-álcool, G-gasolina \n").upper()

preco_gas = 2.50
preco_etanol = 1.90

if comb == 'A':
    preco = litros * preco_etanol
else:
    preco = litros * preco_gas

if litros <= 20:
    preco = preco - (preco*4 / 100)
else:
    preco = preco - (preco * 6 / 100)

print("Total de R${}".format(preco))
