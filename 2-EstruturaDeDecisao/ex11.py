'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

def calculo(sal_atual, perc):
    vl_aumento = (sal_atual * perc) / 100
    novo_sal = float(sal_atual + vl_aumento)
    print("Salário antes do reajuste: R${}".format(sal_atual))
    print("Percentual de aumento aplicado: {}".format(perc))
    print("O Valor do aumento é de R${}".format(vl_aumento))
    print("O novo salário é de R${}".format(novo_sal))

sal_atual = float(input("Informe o salário do colaborador: "))

if sal_atual <= 280:
    calculo(sal_atual, 20)
elif 280 <= sal_atual <= 700:
    calculo(sal_atual, 15)
elif 700 <= sal_atual <= 1500:
    calculo(sal_atual, 10)
elif sal_atual >= 1500:
    calculo(sal_atual, 5)

