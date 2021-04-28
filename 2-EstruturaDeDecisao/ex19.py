'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a
 quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310, 305, 301,
101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''


def divide_centenas(num, casa):
    n = 0
    if casa == 1:
        n = int(num[-1:])
        if n > 1:
            result = " unidades"
        else:
            result = " unidade"
    elif casa == 2:
        n = int(num[1:2])
        if n > 1:
            result = " dezenas"
        else:
            result = " dezena"
    elif casa == 3:
        n = int(num[:1])
        if n > 1:
            result = " centenas"
        else:
            result = " centena"

    return str(n) + result


n = str(input("Informe um numero menor que 1000: "))

if int(n) < 1000:
    cont = 0
    string = ''
    for x in range(0, len(n)):
        cont += 1
        string = divide_centenas(n, cont) + ', ' + string
else:
    print("Informe um numero menor que 1000")

print(string)
