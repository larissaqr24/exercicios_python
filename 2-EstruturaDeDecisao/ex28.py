'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos
tipos de carne da promoção, porém não há limites para a quantidade de carne
 por cliente. Se compra for feita no cartão Tabajara o cliente receberá
 ainda um desconto de 5% sobre o total da compra. Escreva um programa que
 peça o tipo e a quantidade de carne comprada pelo usuário e gere um
 cupom fiscal, contendo as informações da compra: tipo e quantidade de
 carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

tp_carne = input("Informe qual carne deseja: \n"
                 "File Duplo\n"
                 "Alcatra\n"
                 "Picanha\n"
                 ": ").upper()
kilos = float(input("Informe a quantidade de kilos: "))
cartao = input("Pagamento no cartão da loja Tabajaras? \n"
               "Sim - S \n"
               "Não - N \n"
               ": ").upper()

if kilos <= 5:
    if tp_carne == 'FILE DUPLO':
        preco = kilos * 4.90
    elif tp_carne == 'ALCATRA':
        preco = kilos * 5.90
    elif tp_carne == 'PICANHA':
        preco = kilos * 6.90
else:
    if tp_carne == 'FILE DUPLO':
        preco = kilos * 5.80
    elif tp_carne == 'ALCATRA':
        preco = kilos * 6.80
    elif tp_carne == 'PICANHA':
        preco = kilos * 7.80

if cartao == 'S':
    desconto = (preco * 5) / 100
else:
    desconto = 0

print("-" * 40)
print("CUPOM FISCAL")
print("Tipo de carne: {}".format(tp_carne.title()))
print("Quantidade em KG: {} Kg".format(kilos))
print("Preço total: R${}".format(preco))
print("Pagamento no cartão da loja?: {}".format(cartao))
print("Valor do desconto: R${}".format(desconto))
print("Valor a pagar: R${}".format(preco - desconto))
print("-" * 40)
