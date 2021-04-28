'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

l = []
for x in range(4):
    l.append(float(input("Informe a {}ª nota: ".format(x + 1))))

print(l)
print("A média é: {}".format(sum(l) / len(l)))
