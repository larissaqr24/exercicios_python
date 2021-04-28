'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações.'''

nome = 'A'
senha = 'A'

while nome == senha:
    nome = input("Informe o nome de usuario: ")
    senha = input("Informe a senha: ")
    if nome == senha:
        print("Nome de usuario e senha não podem ser iguais!\n"
              "Tente novamente!")
