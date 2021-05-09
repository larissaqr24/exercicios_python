'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem 
inversa a ordem lida.
'''
l = []
for x in range(0, 2):
    l2 = []
    l2.append(input("Informe sua idade: "))
    l2.append(input("Informe sua altura: "))
    l.append(l2)

l.reverse()
for x in l:
    print("Idade: {} \nAltura: {}\n".format(x[0], x[1]))
