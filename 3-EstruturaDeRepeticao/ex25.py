'''Faça um programa que peça para n pessoas a sua idade, ao final o programa
devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e
maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme
a média calculada.'''

print("Digite 999 para sair do programa!")
idade = int(input("informe a idade da 1ª pessoa: "))
list = []
c = 0

while idade != 999:
    if c == 0:
        list.append(idade)
        c += 2
    else:
        idade = int(input("informe a idade da {}ª pessoa: ".format(c)))
        list.append(idade)
        c += 1

list.remove(999)
media = sum(list) / len(list)

if 0 <= media <= 25:
    turma = "jovem"
elif 26 <= media <= 60:
    turma = "adulta"
else:
    turma = "idosa"

print("A turma é {}!".format(turma))
