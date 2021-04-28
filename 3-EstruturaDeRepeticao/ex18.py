'''Faça um programa que, dado um conjunto de N números, determine o menor
valor, o maior valor e a soma dos valores.'''

n = int(input("Informe quantos numeros desejar, para encerrar, digite 999: "))
list = []
c = 0
while n != 999:
    if c == 0:
        list.append(n)
        c += 1
    else:
        n = int(input("Informe quantos numeros desejar, para encerrar, "
                      "digite 999: "))
        list.append(n)

list.remove(999)
list.sort(reverse=True)
maior = list[0]
list.sort()
menor = list[0]
print("Lista completa: {}\n"
      "Menor numero: {}\n"
      "Maior numero: {}\n"
      "Soma dos dois numeros {}\n"
      "Soma de toda a lista: {}".format(list, menor, maior, (menor + maior),
                                        sum(list)))
