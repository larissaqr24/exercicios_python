'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes
foram lidas.
Imprima as consoantes.
'''

l = []
vogais = ['A', 'E', 'I', 'O', 'U']

for x in range(10):
    l.append(str(input("Informe a {}º caractere: ".format(x + 1))).upper())

lista_final = [x for x in l if x not in vogais]
print(lista_final)
print("Existe {} consoantes!".format(len(lista_final)))
