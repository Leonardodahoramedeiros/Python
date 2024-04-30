Nome = str(input("Digite seu nome: ")).strip()

print("Seu nome em letras maiusculas é {}".format(Nome.upper()))
print("Seu nome em letrar minusculas é {}".format(Nome.lower()))
print("Seu nome tem {} letras!".format(len(Nome)))

print("Seu primeiro nome tem {} letras.".format(Nome.find(' ')))