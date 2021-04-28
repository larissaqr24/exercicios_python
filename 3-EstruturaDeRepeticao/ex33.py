'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas, e informe ao
final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.'''

list = []

t = 0
while t != 999:
    t = float(input("Informe uma temperatura ou digite 999 para sair: "))
    list.append(t)


list.remove(999)
list.sort()
min = list[0]
list.sort(reverse=True)
max = list[0]

print("Menor temperatura: {}\n"
      "Maior temperatura: {}\n"
      "Média: {}".format(min, max, sum(list) / len(list)))
