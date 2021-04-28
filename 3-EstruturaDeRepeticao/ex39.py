'''Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando a sua altura em
centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do
aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''

alt_maior = 0
alt_menor = 999

for x in range(10):
    num_aluno = int(input("Informe o numero do aluno: "))
    alt_cm = float(input("Informe a altura do aluno {}: ".format(num_aluno)))

    if alt_cm > alt_maior:
        alt_maior = alt_cm
        cd_maior = num_aluno

    if alt_cm < alt_menor:
        alt_menor = alt_cm
        cd_menor = num_aluno


print("Aluno mais alto\n"
      "Código: {}\n"
      "Altura: {}\n"
      "\n"
      "Aluno mais baixo\n"
      "Código: {}\n"
      "Altura: {}".format(cd_maior, alt_maior, cd_menor,alt_menor))
