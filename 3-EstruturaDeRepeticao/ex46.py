'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos
No final da série de saltos de cada atleta, o melhor e o pior resultados são
eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe a média dos saltos conforme a
descrição acima informada (retirar o melhor e o pior salto e depois calcular
a média). Faça uso de uma lista para armazenar os saltos. Os saltos são
informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''


def salto_atleta(atleta):
    l = []
    for x in range(1, 6):
        l.append(float(input("Informe o valor do {}º salto: ".format(x))))

    primeiro = l[0]
    segundo = l[1]
    terceiro = l[2]
    quarto = l[3]
    quinto = l[4]
    l.sort()
    menor = l[0]
    maior = l[4]
    l.pop(0)
    l.pop()
    media = round(sum(l) / len(l), 2)
    print('Atleta: {}\n\n'
          'Primeiro Salto: {} m\n'
          'Segundo Salto: {} m\n'
          'Terceiro Salto: {} m\n'
          'Quarto Salto: {} m\n'
          'Quinto Salto: {} m\n\n'
          'Melhor Salto: {} m\n'
          'Pior Salto: {} m\n'
          'Média dos demais saltos: {} m\n\n'
          'Resultado Final: \n'
          '{}: {} m'.format(atleta, primeiro, segundo, terceiro, quarto, quinto, maior, menor, media, atleta, media))


nome = 'a'

while nome != '':
    nome = str(input("Informe o nome do atleta: "))
    if nome != '':
        salto_atleta(nome)
