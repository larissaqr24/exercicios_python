'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99
e agora possui uma loja de conveniências. Faça um programa que implemente uma
caixa registradora rudimentar. O programa deverá receber um número
desconhecido de valores referentes aos preços das mercadorias. Um valor zero
deve ser informado pelo operador para indicar o final da compra. O programa
deve então mostrar o total da compra e perguntar o valor em dinheiro que o
cliente forneceu, para então calcular e mostrar o valor do troco. Após esta
operação, o programa deverá voltar ao ponto inicial, para registrar a próxima
compra. A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
'''


def compras():
    l = []
    n = 1
    while n != 0:
        n = float(input("Informe o valor do produto: "))
        l.append(n)

    l.remove(0)
    return l


list = compras()
valor = float(input("Informe a quantidade em dinheiro do cliente: "))

while valor < sum(list):
    print("O valor informado é menor que a quantidade total da compra: ")
    valor = float(input("Informe a quantidade em dinheiro do cliente: "))

print("\nLojas Tabajara")
for x in range(0, len(list)):
    print("Produto {}: R$ {}".format(x + 1, list[x]))

print("Total: R${}\n"
      "Dinheiro: R${}\n"
      "Troco: R${}".format(sum(list), valor, (valor-sum(list))))
