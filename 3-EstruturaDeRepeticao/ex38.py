'''Um funcionário de uma empresa recebe aumento salarial anualmente:
Sabe-se que:
a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o
salário inicial do funcionário.'''

from datetime import date


def ajuste_salarial(salario, perc):
    new_salario = ((salario * perc) / 100) + salario
    return new_salario


ano_inicial = 1995
sal_inicial = float(input("Informe o salário inicial: "))
perc_inicial = 1.5
data = date.today()
ano_atual = data.year
cont = 0

for x in range(ano_inicial, ano_atual + 1):
    if cont == 1:
        new_salario = ajuste_salarial(sal_inicial, perc_inicial)
        new_perc = perc_inicial
    elif cont > 1:
        new_perc = new_perc * 2
        new_salario = ajuste_salarial(new_salario, new_perc)
        print('-' * 50)
        print(x)
        print(new_perc)
        print(new_salario)
    cont += 1

print(new_salario)
