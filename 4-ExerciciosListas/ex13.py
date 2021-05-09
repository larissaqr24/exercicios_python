'''Faça um programa que receba a temperatura média de cada mês do ano
 e armazene-as em uma lista. Após isto, calcule a média anual das
 temperaturas e mostre todas as temperaturas acima da média anual,
 e em que mês elas ocorreram 
 (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

# dicTemp = {'Janeiro': 0,
#            'Fevereiro': 0,
#            'Março': 0,
#            'Abril': 0,
#            'Maio': 0,
#            'Junho': 0,
#            'Julho': 0,
#            'Agosto': 0,
#            'Setembro': 0,
#            'Outubro': 0,
#            'Novembro': 0,
#            'Dezembro': 0}

dicTemp = {'Janeiro': 35.0, 'Fevereiro': 35.6, 'Março': 40.0, 'Abril': 34.0, 'Maio': 30.0, 'Junho': 20.0,
           'Julho': 15.0, 'Agosto': 19.0, 'Setembro': 25.0, 'Outubro': 30.0, 'Novembro': 31.0, 'Dezembro': 34.5}

# print(dicTemp)
med = 0
for x in dicTemp:
    #temp = float(input("Informe a temperatura média do mês de {}: ".format(x)))
    #dicTemp[x] = temp
    print(dicTemp[x])
    #med = med + temp
    med = med + dicTemp[x]

med = round(med / len(dicTemp), 2)
print("Meses com a média acima da anual ({}):".format(med))
for x in dicTemp:
    if dicTemp[x] > med:
        print('{} = {}'.format(x, dicTemp[x]))
