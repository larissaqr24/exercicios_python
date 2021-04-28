'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
quantidade (em Kg) de maças adquiridas e escreva o valor a ser
pago pelo cliente.
'''

kg_morango = float(input("Informe a quantide de KG de morangos: "))
kg_maca = float(input("Informe a quantide de KG de maças: "))
total_kg = kg_morango + kg_maca

if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

preco_total = (preco_morango + preco_maca)

if total_kg > 8 or preco_total > 25:
    preco_total = preco_total - (preco_total * 10 / 100)

print("Valor total de R${}".format(preco_total))
