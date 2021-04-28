'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
12376489
  => 98467321
'''

n = int(input("Informe um numero inteiro positivo: "))

if n < 0:
    print("O numero deve ser positivo!")
else:
    new = str(n)
    rev = ''
    for x in range(1, len(new) + 1):
        rev += new[-x]

    print(rev)  # pelo loop
    print(new[::-1])  # modo izi

# new = '12376489'
# print(len(new))
# print(new[-7])
#
