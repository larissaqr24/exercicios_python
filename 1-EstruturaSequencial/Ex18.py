'''Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps)
, calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tam_arquivo = int(input("Informe o tamanho do arquivo em MB: "))
vel_mbps = int(input("Informe sua velocidade de internet em Mbps: "))

seg = tam_arquivo / (vel_mbps / 8)
min = round(seg / 60)

print("Aproximadamente {} minutos.".format(min))
