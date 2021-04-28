'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo
Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = float((n1+n2) / 2)

if media <= 4:
    conceito = "E"
elif 4.1 <= media <= 6:
    conceito = "D"
elif 6.1 <= media <= 7.5:
    conceito = "C"
elif 7.6 <= media <= 9:
    conceito = "B"
elif 9.1 <= media <= 10:
    conceito = "A"

if conceito in ("A", "B", "C"):
    result = "APROVADO"
else:
    result = "REPROVADO"

print("Notas: {} e {}".format(n1, n2))
print("Média: {}".format(media))
print("Conceito: {}".format(conceito))
print("{}".format(result))
