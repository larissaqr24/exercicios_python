'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
l = []

for x in range(5):
    l.append(float(input('Numero ' + str(x + 1) + ': ')))

l.reverse()
print(l)
