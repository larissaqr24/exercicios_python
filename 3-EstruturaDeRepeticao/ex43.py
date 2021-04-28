'''O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades
desejadas.Calcule e mostre o valor a ser pago por item (preço * quantidade)
e o total geral do pedido. Considere que o cliente deve informar quando o
pedido deve ser encerrado.
'''

n = 1
qt_hot_dog = 0
qt_bauru = 0
qt_bauru_ovo = 0
qt_hamburger = 0
qt_xburger = 0
qt_refri = 0

cons_hot_dog = 1.20
cons_bauru = 1.30
cons_bauru_ovo = 1.50
cons_hamburger = 1.20
cons_xburger = 1.30
cons_refri = 1.00
vl_hot_dog = vl_bauru = vl_bauru_ovo = vl_hamburger = vl_xburger = vl_refri = 0.00

while n != 0:
    n = int(input("Informe um código do produto: "))
    if n != 0:
        qt = int(input("Quantas unidades?: "))

        if n == 100:
            qt_hot_dog = qt_hot_dog + qt
            vl_hot_dog = cons_hot_dog * qt_hot_dog
        elif n == 101:
            qt_bauru += 1
            vl_bauru = cons_bauru * qt_bauru
        elif n == 102:
            qt_bauru_ovo += 1
            vl_bauru_ovo = cons_bauru_ovo * qt_bauru_ovo
        elif n == 103:
            qt_hamburger += 1
            vl_hamburger = cons_hamburger * qt_hamburger
        elif n == 104:
            qt_xburger += 1
            vl_xburger = cons_xburger * qt_xburger
        elif n == 105:
            qt_refri += 1
            vl_refri = cons_refri * qt_refri
        else:
            print('Produto não cadastrado!')

vl_total = vl_hot_dog + vl_bauru + vl_bauru_ovo + vl_hamburger + vl_xburger + vl_refri

print('{:>20} | {:>20} | {:>20}'.format('Produto', 'Quantidade', 'Sub-Total'))
if vl_hot_dog > 0:
    print('{:>20} | {:>20} | {:>20}'.format('Cachorro Quente', qt_hot_dog, vl_hot_dog))
if vl_bauru > 0:
    print('{:>20} | {:>20} | {:>20}'.format('Bauru Simples', qt_bauru, vl_bauru))
if vl_bauru_ovo > 0:
    print('{:>20} | {:>20} | {:>20}'.format('Bauru com ovo', qt_bauru_ovo, vl_bauru_ovo))
if vl_hamburger > 0:
    print('{:>20} | {:>20} | {:>20}'.format('Hamburguer', qt_hamburger, vl_hamburger))
if vl_xburger > 0:
    print('{:>20} | {:>20} | {:>20}'.format('Cheeseburguer', qt_xburger, vl_xburger))
if vl_refri > 0:
    print('{:>20} | {:>20} | {:>20}'.format('Refrigerante', qt_refri, vl_refri))

print('-' * 40)
print('Total a pagar: R${}'.format(vl_total))
