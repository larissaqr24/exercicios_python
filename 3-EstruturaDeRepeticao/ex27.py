'''Faça um programa que calcule o número médio de alunos por turma. Para isto,
peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.'''

qtd_turma = int(input("Informe a quantidade de turmas: "))
qtd_total = 0
for x in range(1, qtd_turma + 1):
    qtd_alunos = int(input("Informe a quantidade de alunos da {}ª turma: ".format(x)))
    while qtd_alunos > 40:
        print("Quantida maxima é de 40 alunos!")
        qtd_alunos = int(input("Informe a quantidade de alunos da {}ª turma: ".format(x)))

    qtd_total = qtd_total + qtd_alunos

print("A média de alunos das {} turmas é de: {}".format(qtd_turma, qtd_total / qtd_turma))
