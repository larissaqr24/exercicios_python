'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados
por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o
conjunto de votos tem-se o valor zero.
'''

n = 999
c1 = 0
c2 = 0
c3 = 0
c4 = 0
nulo = 0
branco = 0

while n != 0:
    n = int(input("Informe o numero do seu candidato sendo eles\n"
                  "1 - José\n"
                  "2 - João\n"
                  "3 - Maria\n"
                  "4 - Claudia\n"
                  "5 - Valo Nulo\n"
                  "6 - Voto em Branco\n"
                  "0 - Para encerrar\n"
                  ": "))

    if n == 1:
        c1 += 1
    elif n == 2:
        c2 += 1
    elif n == 3:
        c3 += 1
    elif n == 4:
        c4 += 1
    elif n == 5:
        nulo += 1
    elif n == 6:
        branco += 1
    elif n == 0:
        pass
    else:
        print("Opção Inválida!")


print('Resultado Eleições 2020')
print('{:>20} | {:>20}'.format('Candidato', 'Total de votos'))
print('{:>20} | {:>20}'.format('José', c1))
print('{:>20} | {:>20}'.format('João', c2))
print('{:>20} | {:>20}'.format('Maria', c3))
print('{:>20} | {:>20}'.format('Claudia', c4))
print('Votos nulos: {}'.format(nulo))
print('Votos em branco: {}'.format(branco))
print('A percentagem de votos nulos sobre o total de votos: {}%'.format((c1+c2+c3+c4+nulo+branco)*nulo / 100))
print('A percentagem de votos em branco sobre o total de votos: {}%'.format((c1+c2+c3+c4+nulo+branco)*branco / 100))
