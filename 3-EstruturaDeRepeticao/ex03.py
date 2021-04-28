'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''


nome = input("Informe seu nome: ")
while len(nome) <= 3:
    nome = input("Informe seu nome: ")

idade = int(input("Informe sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Informe sua idade: "))

salario = float(input("Informe o salário: "))
while salario <= 0:
    salario = float(input("Informe o salário: "))

sexo = input("Informe o sexo\n"
             "F - Feminino\n"
             "M - Masculinho\n"
             ": ").upper()

while sexo not in ('F', 'M'):
    sexo = input("Informe o sexo\n"
                 "F - Feminino\n"
                 "M - Masculinho\n"
                 ": ").upper()

civil = input("Informe o estado civil.\n"
              "S - Solteiro\n"
              "C - Casado\n"
              "V - Viuvo\n"
              "D - Divorciado\n"
              ":").upper()

while civil not in ('S', 'C', 'V', 'D'):
    civil = input("Informe o estado civil.\n"
                  "S - Solteiro\n"
                  "C - Casado\n"
                  "V - Viuvo\n"
                  "D - Divorciado\n"
                  ":").upper()

print("Cadastro realizado! \n"
      "Nome: {}\n"
      "Idade: {}\n"
      "Salário: {}\n"
      "Sexo: {}\n"
      "Estado Civil: {}".format(nome, idade, salario, sexo, civil))
