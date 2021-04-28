'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e
armazene num vetor a média de cada aluno,  imprima o número de alunos
com média maior ou igual a 7.0.'''

media = []
cont = 0

for x in range(1, 4):
    total = 0
    for y in range(1, 5):
        nota = int(input("Informe a {}ª nota do aluno {}: ".format(y, x)))
        total = total + nota
    media.append(int(total/4))
for z in media:
    if z >= 7:
        cont += 1

print('{} alunos estão com a média maior ou igual a 7'.format(cont))
