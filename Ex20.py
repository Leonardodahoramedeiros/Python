Nome = str(input("Digite seu nome: ")).strip()

print("Seu nome em letras maiusculas é {}".format(Nome.upper()))
print("Seu nome em letrar minusculas é {}".format(Nome.lower()))
print("Seu nome tem {} letras!".format(len(Nome) - Nome.count(' ')))

print("Seu primeiro nome tem {} letras.".format(Nome.find(' ')))
separa = Nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))