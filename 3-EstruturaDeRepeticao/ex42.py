'''Faça um programa que leia uma quantidade indeterminada de números positivos
e conte quantos deles estão nos seguintes intervalos:
[0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.'''

x = -1
n = 0
l1 = []
l2 = []
l3 = []
l4 = []

while x < n:
    n = int(input("Informe um numero: "))

    if 0 <= n <= 25:
        l1.append(n)
    elif 26 <= n <= 50:
        l2.append(n)
    elif 51 <= n <= 75:
        l3.append(n)
    elif 76 <= n <= 100:
        l4.append(n)

print('\nListas')
print('{}, {}, {}, {}'.format(l1, l2, l3, l4))
print('\nQuantidades:')
print('[0-25]: {}\n'
      '[26-50]: {}\n'
      '[51-75]: {}\n'
      '[76-100]: {}\n'.format(len(l1), len(l2), len(l3), len(l4), ))
