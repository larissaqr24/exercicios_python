'''Numa eleição existem três candidatos. Faça um programa que peça o número
total de eleitores. Peça para cada eleitor votar e ao final mostrar o número
de votos de cada candidato.'''

c1 = 0
c2 = 0
c3 = 0

eleitores = int(input("Informe o numero total de eleitores: "))

for x in range(1, eleitores + 1):
    n = int(input("Qual dos 3 candidatos é o seu voto?\n"
                  "1 - Fulano\n"
                  "2 - Ciclano\n"
                  "3 - Beltrano"
                  ": "))

    if n == 1:
        c1 += 1
    elif n == 2:
        c2 += 1
    elif n == 3:
        c3 += 1
    else:
        print("Voto Nulo!")

print("Resultado da Eleieção!\n"
      "Fulano. Votos: {}\n"
      "Ciclano. Votos: {}\n"
      "Beltrano. Votos: {}".format(c1, c2, c3))

