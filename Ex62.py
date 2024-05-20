sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos. Digite seu sexo: ")).strip().upper()[0] # serve para fatiar a string 
print("Sexo {} resgitrado com sucesso".format(sexo))

