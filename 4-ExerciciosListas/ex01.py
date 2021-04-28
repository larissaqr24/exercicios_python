'''
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''
l = []

for x in range(5):
    l.append(int(input('Numero ' + str(x + 1) + ': ')))
print(l)
