'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,..
Faça um programa que gere a série até que o valor seja maior que 500.'''

f1 = 1
f2 = 1
c = 0
list = [0, 1, 1]

while c <= 500:
    c = f1 + f2
    f1 = c
    f2 = (c - f2)
    list.append(c)

print(list)
