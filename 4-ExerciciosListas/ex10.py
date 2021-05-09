'''Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser
 compostos pelos elementos intercalados dos dois outros vetores'''

l1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
l2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
l3 = []

for x in range(0, 10):
    l3.append(l1[x])
    l3.append(l2[x])

print(l3)
