'''Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.'''

l1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
l2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
l3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
l4 = []

# Gera Listas
# inc = 3
# for ini in range(1, 4):
#     l = []
#     for x in range(1, 11):
#         l.append(ini)
#         ini = ini+inc
#     print(l)

for x in range(0, 10):
    l4.append(l1[x])
    l4.append(l2[x])
    l4.append(l3[x])


print(l4)
