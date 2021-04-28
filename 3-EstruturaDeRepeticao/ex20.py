'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular
o fatorial várias vezes e limitando o fatorial a números inteiros positivos
e menores que 16.'''


n = int(input("Informe um numero inteiro positivo até 16, para encerrar digite 999: "))

while n != 999:

    if n < 1 or n > 16:
        n = int(input("Informe um numero inteiro positivo até 16, para encerrar digite 999: "))
    else:
        n_fat = 1
        for x in range(1, n+1):
            n_fat = n_fat * x

        print(n_fat)
        n = int(input("Informe um numero inteiro positivo até 16, para encerrar digite 999: "))
