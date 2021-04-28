'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a
 quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310, 305, 301,
101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

n = str(input("Informe um numero menor que 1000: "))

if int(n) < 1000:
    if len(n) == 1:
        if n[2:3] <= 1:
            unidade = str(n[2:3]) + "unidade"
        else:
            unidade = str(n[2:3]) + "unidades"
    elif len(n) == 2:
        if n[1:2] <= str(1):
            print("{} dezena{} unidade".format(n[1:2]))
        else:
            print("{} unidades".format(n[1:2]))
    elif len(n) == 3:
        if n[1:2] <= 1:
            print("{} unidade".format(n[0:1]))
        else:
            print("{} unidades".format(n[0:1]))
else:
    print("Informe um numero menor que 1000")

