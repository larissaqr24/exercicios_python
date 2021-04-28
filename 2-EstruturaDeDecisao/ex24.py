'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação
ele deseja realizar. O resultado da operação deve ser acompanhado de uma
frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

n1 = float(input("Informe um numero: "))
n2 = float(input("Informe um segundo numero: "))

print('Informe qual operação deseja')
op = int(input('1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divição'))

if op == 1:
    result = n1 + n2
elif op == 2:
    result = n1 - n2
elif op == 3:
    result = n1 * n2
elif op == 4:
    result = n1 / n2

if result % 2 == 0:
    frase = "Par"
else:
    frase = "Impar"

if result >= 0:
    frase = frase + ", positivo"
else:
    frase = frase + ", negativo"

if int(result) == result:
    frase = frase + " e inteiro"
else:
    frase = frase + " e decimal"

print("{} é {}".format(result, frase))