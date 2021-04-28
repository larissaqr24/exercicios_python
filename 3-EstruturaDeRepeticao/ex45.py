'''
Desenvolver um programa para verificar a nota do aluno em uma prova com
10 questões, o programa deve perguntar ao aluno a resposta de cada questão e
ao final comparar com o gabarito da prova e assim calcular o total de acertos
e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o
sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o
professor digite o gabarito da prova antes dos alunos usarem o programa.
'''


def prova_aluno():
    acerto = 0
    for x in range(1, 11):
        r = input(str("Resposta da alternativa {}: ".format(x))).upper()
        if r == gab[x - 1]:
            acerto += 1

    notas_geral.append(acerto)


gab = []
notas_geral = [9, 10, 5]
#gab = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
n = 'S'

print("Professor, preencher o gabarito da prova.")
for x in range(1, 11):
    resp = input(str("{} = : ".format(x))).upper()
    gab.append(resp)


while n != 'N':
    prova_aluno()
    n = input(str("Tem outro aluno para responder? (S/N): ")).upper()


print('-' * 50)
notas_geral.sort()
menor_nota = notas_geral[0]
notas_geral.sort(reverse=True)
maior_nota = notas_geral[0]
print('Menor nota: {}\n'
      'Maior nota: {}'.format(menor_nota, maior_nota))
print('Total de Alunos que utilizaram o sistema: {}'.format(len(notas_geral)))

print('Média das Notas da Turma: {}'.format(sum(notas_geral) / len(notas_geral)))


