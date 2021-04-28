'''Uma academia deseja fazer um senso entre seus clientes para descobrir o
mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve
fazer um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso. O final da digitação de dados deve ser dada quando o
usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve
ser informados os códigos e valores do clente mais alto, do mais baixo, do
mais gordo e do mais magro, além da média das alturas e dos pesos dos
clientes'''


cod = -1
l_codigo = []
l_altura = []
l_peso = []

while cod != 0:
    cod = int(input("Informe o código do usuario: "))
    if cod == 0:
        break
    else:
        l_codigo.append(cod)
        altura = float(input("Informe sua altura: "))
        l_altura.append(altura)
        peso = float(input("Informe seu peso: "))
        l_peso.append(peso)


cod_magro = l_peso.index(min(l_peso))
cod_gordo = l_peso.index(max(l_peso))
cod_alto = l_altura.index(max(l_altura))
cod_baixo = l_altura.index(min(l_altura))

print("Código do mais magro: ", l_codigo[cod_magro])
print("Código do mais gordo: ", l_codigo[cod_gordo])
print("Código do mais alto: ", l_codigo[cod_alto])
print("Código do mais baixo: ", l_codigo[cod_baixo])
print("Média de altura: ", sum(l_altura) / len(l_altura))
print("Média de peso: ", sum(l_peso) / len(l_peso))
