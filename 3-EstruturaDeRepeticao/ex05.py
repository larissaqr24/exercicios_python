'''Altere o programa anterior permitindo ao usuário informar as populações e
as taxas de crescimento iniciais. Valide a entrada e permita repetir a
operação.'''

hab_a = int(input("Informe a população do pais A: "))
hab_b = int(input("Informe a população do pais B: "))
taxa_a = float(input("Informe a taxa de crescimento do pais A: "))
taxa_b = float(input("Informe a taxa de crescimento do pais B: "))
ano = 0

while hab_a <= hab_b:
    hab_a = hab_a + (hab_a * taxa_a / 100)
    hab_b = hab_b + (hab_b * taxa_b / 100)
    ano += 1

print("Pais A vai demorar {} anos para ultrapassar ou igualar o pais B".format(ano))
