'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''

n = int(input("Informe um numero inteiro: "))
print("Fatorial de : {}".format(n))
txt = '{}! = '.format(n)
n_fat = 1
for x in range(n, 0, -1):
    if x == 1:
        txt = txt + ' {} = '.format(x)
    else:
        txt = txt + ' {} .'.format(x)

    n_fat = n_fat * x

print(txt + str(n_fat))
