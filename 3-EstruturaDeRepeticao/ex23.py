'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário. O programa deverá mostrar também o número de
divisões que ele executou para encontrar os números primos. Serão avaliados
o funcionamento, o estilo e o número de testes (divisões) executados.'''

n = int(input("Informe um numero inteiro: "))
cont = 0
l_primo = []
l_div = []
for z in range(1, n+1):
    cont = 0
    for x in range(1, z+1):
        if z % x == 0:
            cont += 1
    if cont == 2:
        l_primo.append(z)


print(l_primo)



