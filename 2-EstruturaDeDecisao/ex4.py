'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = input("Informe uma letra: ").upper()
vogais = ['A', 'E', 'I', 'O', 'U']

if letra.isdigit():
    print("Informe uma letra!")
elif letra.__len__() != 1:
    print("Informe apenas uma letra!")
else:
    if letra in vogais:
        print("É vogal")
    else:
        print("É consoante")