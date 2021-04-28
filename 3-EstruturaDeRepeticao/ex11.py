'''Altere o programa anterior para mostrar no final a soma dos números.'''

n1 = int(input("Informe um numero: "))
n2 = int(input("Informe outro numero: "))

list = []
for x in range(n1+1, n2):
    list.append(x)

print(list)
print(sum(list))
