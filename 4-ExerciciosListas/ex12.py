'''Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos
possuem altura inferior à média de altura desses alunos'''

import random

l = [[12, 1.58], [11, 1.66], [12, 1.54], [13, 1.49], [8, 1.63], [10, 1.65], [12, 1.55], [8, 1.57], [9, 1.68], [13, 1.53], [9, 1.58], [12, 1.62], [13, 1.68], [8, 1.61], [10, 1.54],
     [8, 1.62], [7, 1.62], [12, 1.47], [10, 1.54], [14, 1.54], [7, 1.6], [14, 1.49], [8, 1.61], [11, 1.57], [9, 1.62], [11, 1.62], [7, 1.66], [9, 1.5], [13, 1.67], [13, 1.65]]
# l = []
# for x in range(1, 31):
#     temp = []
#     temp.append(random.randrange(7, 15))
#     temp.append(round(random.uniform(1.45, 1.70), 2))
#     l.append(temp)

# print(l)

med_altura = 0
for x in l:
    med_altura = med_altura + x[1]

med_altura = round(med_altura/l.__len__(), 2)

cont = 0
for x in l:
    if x[0] > 13 and x[1] < med_altura:
        cont += 1

print("Quantidade: " + str(cont))
