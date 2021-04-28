'''Encontrar números primos é uma tarefa difícil. Faça um programa que gera
uma lista dos números primos existentes entre 1 e um número inteiro
informado pelo usuário.'''


def primo(num):
    cont = 0
    for x in range(1, num + 1):
        if num % x == 0:
            cont += 1

    if cont == 2:
        return True


list = []
n = int(input("Informe um numero inteiro: "))

for x in range(1, n+1):
    if primo(x):
        list.append(x)

print("Os numeros primos de 1 até {} são: \n"
      "{}".format(n, list))
