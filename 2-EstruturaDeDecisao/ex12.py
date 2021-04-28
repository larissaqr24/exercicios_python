'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS
corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor
da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo
. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00
(-) INSS ( 10%)                 : R$  110,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  165,00
Salário Liquido                 : R$  935,00
'''

def calculo_folha(vl_hora, qt_horas):
    sal_bruto = float(qt_horas * vl_hora)
    if sal_bruto <= 900:
        perc_ir = 0
    elif sal_bruto <= 1500:
        perc_ir = 5
    elif sal_bruto <= 2500:
        perc_ir = 10
    else:
        perc_ir = 20

    vl_ir = float((sal_bruto * perc_ir) / 100)
    vl_inss = float((sal_bruto * 10) / 100)
    vl_fgts = float((sal_bruto * 11) / 100)
    print("Salário Bruno: ({} * {})      : R$ {}".format(qt_horas, vl_hora, sal_bruto))
    print("(-) IR ({})                   : R$ {}".format(perc_ir, vl_ir))
    print("(-) INSS (10%)                : R$ {}".format(vl_inss))
    print("FGTS (11%)                    : R$ {}".format(vl_fgts))
    print("Total de descontos            : R$ {}".format(float(vl_ir + vl_inss)))
    print("Salário Liquido               : R$ {}".format(float(sal_bruto - (vl_ir + vl_inss))))

vl_hora = float(input("Informe o valor da hora: "))
qt_horas = float(input("Informe a quantidade de horas trabalhadas: "))
calculo_folha(vl_hora, qt_horas)

