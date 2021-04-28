'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual numero ele
deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''

n = int(input("Informe qual tabuada deseja, entre 1 a 10: "))
while n < 1 or n > 10:
    n = int(input("Informe qual tabuada deseja, entre 1 a 10: "))

print("Tabuada de {}".format(n))
for x in range(1, 11):
    print("{} x {:2} = {:2}".format(n, x, (n * x)))
