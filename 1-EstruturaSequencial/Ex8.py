# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Informe o valor da sua hora de trabalho: "))
qtd_hora = float(input("Informe a quantidade de horas trabalhadas no mês: "))

print("Seu salário é: " + str(valor_hora * qtd_hora))
