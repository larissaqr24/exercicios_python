# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''
n1 = int(input("Informe a 1ª nota: "))
n2 = int(input("Informe a 2ª nota: "))
n3 = int(input("Informe a 3ª nota: "))
n4 = int(input("Informe a 4ª nota: "))
print("Sua média é: " + str(((n1+n2+n3+n4)/4)))
'''

cont = 0
total = 0
while(cont < 4):
    cont += 1
    total = total + (int(input("Informe a "+str(cont)+"ª nota: ")))
print("Sua média é: " + str(total/cont))
