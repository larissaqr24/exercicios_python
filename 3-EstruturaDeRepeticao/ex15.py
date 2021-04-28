'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
 Faça um programa capaz de gerar a série até o n−ésimo termo.'''


n = int(input('Informe um numero: '))

f1 = 1
f2 = 1
c = 0

list = [0, 1, 1]

for x in range(0, n):
    c = f1 + f2
    f1 = c
    f2 = (c - f2)
    list.append(c)

print(list)
