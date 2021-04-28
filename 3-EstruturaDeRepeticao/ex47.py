'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos
votos restantes. Você deve fazer um programa que receba o nome do ginasta e as
notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois
informe a sua média, conforme a descrição acima informada (retirar o melhor e
o pior salto e depois calcular a média com as notas restantes). As notas não
são informados ordenadas. Um exemplo de saída do programa deve ser conforme
o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''


def calc_nota(atleta):
    l = []
    for x in range(1, 8):
        l.append(float(input("Informe a {}º nota: ".format(x))))

    l.sort()
    pior = l[0]
    melhor = l[6]
    l.pop(0)
    l.pop()
    media = round(sum(l) / len(l), 2)

    print('Resultado final:\n'
          'Atleta: {}\n'
          'Melhor nota: {}\n'
          'Pior nota: {}\n'
          'Média: {}'.format(atleta, melhor, pior, media))


nome = 's'

while nome != '':
    nome = str(input("Informe o nome do Atleta: "))
    if nome != '':
        calc_nota(nome)
