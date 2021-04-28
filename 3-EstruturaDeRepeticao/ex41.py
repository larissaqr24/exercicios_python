'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com
os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas
e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  || % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
'''


vl_divida = float(input("Informe o valor da divida: "))

print('{:>25} | {:>25} | {:>25} | {:>25}'.format('Valor da Dívida', 'Valor dos Juros', 'Quantidade de Parcelas', 'Valor da Parcela'))
print('{:>25} | {:>25} | {:>25} | {:>25}'.format(vl_divida, 0, 1, vl_divida))
for x in range(3, 13, 3):
    if x == 3:
        vl_juros = (vl_divida * 10) / 100
    elif x == 6:
        vl_juros = (vl_divida * 15) / 100
    elif x == 9:
        vl_juros = (vl_divida * 20) / 100
    elif x == 12:
        vl_juros = (vl_divida * 25) / 100

    print('{:>25} | {:>25} | {:>25} | {:>25}'.format((vl_divida + vl_juros), vl_juros, x, (vl_divida + vl_juros)/x))
