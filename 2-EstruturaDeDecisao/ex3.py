'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

s = input("Informe a sigla do sexo: ").upper()
if s == 'F':
    print("Feminino")
elif s == 'M':
    print("Masculino")
else:
    print("Sexo Inválido")
