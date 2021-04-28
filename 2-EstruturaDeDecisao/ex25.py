'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a
2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".'''

p1 = input("Telefonou para a vítima? S ou N").upper()
p2 = input("Esteve no local do crime? S ou N").upper()
p3 = input("Mora perto da vítima? S ou N").upper()
p4 = input("Devia para a vítima? S ou N").upper()
p5 = input("Já trabalhou com a vítima? S ou N").upper()

cont = 0

if p1 == 'S':
    cont += 1
if p2 == 'S':
    cont += 1
if p3 == 'S':
    cont += 1
if p4 == 'S':
    cont += 1
if p5 == 'S':
    cont += 1

if cont == 5:
    print("Assassino")
if cont == 3 or cont == 4:
    print("Cúmplice")
if cont == 2:
    print("Suspeita")
else:
    print("Inocente")
