'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados
sobre acidentes de trânsito. Foram obtidos os seguintes dados:
a. Código da cidade;
b. Número de veículos de passeio (em 1999);
c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d. Qual o maior e menor índice de acidentes de transito e a que cidade
    pertence;
e. Qual a média de veículos nas cinco cidades juntas;
f. Qual a média de acidentes de trânsito nas cidades com menos de
    2.000 veículos de passeio.'''

maior_acid = soma = soma2 = count = 0
menor_acid = 9999

for x in range(1, 6):
    cd_city = int(input("Informe o código da cidade: "))
    qt_veiculo = int(input("Informe a quantidade de veiculos: "))
    qt_acidente = int(input("Informe a quantidade de acidentes: "))

    soma += qt_veiculo

    if qt_acidente > maior_acid:
        maior_acid = qt_acidente
        maior_city = cd_city

    if qt_acidente < menor_acid:
        menor_acid = qt_acidente
        menor_city = cd_city

    if qt_veiculo < 2000:
        count += 1
        soma2 += qt_acidente

print("Maior indice de acidentes:\n"
      "Cidade: {}\n"
      "Quantidade: {}\n".format(maior_city, maior_acid))

print("Menor indice de acidentes:\n"
      "Cidade: {}\n"
      "Quantidade: {}\n".format(menor_city, menor_acid))

print("Média de veiculos nas cinco cidades: {}".format(soma/5))
print("Média de acidentes nas cidades com menos de 2000 veiculos: {}".format(soma2/count))
