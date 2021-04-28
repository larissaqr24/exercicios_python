'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
 mesma é uma data válida.'''
import datetime


def verifica_data(dia, mes, ano, valida=None):
    try:
        data == datetime.datetime(ano, mes, dia)
        valida = True
    except ValueError:
        valida = False
    return valida


data = str(input("Informe a data no formato dd/mm/aaaa: "))
dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[-4:])
print(verifica_data(dia, mes, ano))
