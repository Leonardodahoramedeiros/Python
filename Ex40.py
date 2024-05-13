Nome = str(input("Digite seu nome: "))

if Nome == 'Gustavo':
    print("Que nome Bonito você tem!")
elif Nome == 'Maria' or Nome == 'Leonardo' or Nome == 'Josiane':
    print("Seu nome é porpular no Brasil!")
elif Nome in 'Ana Claudia Jessica':
    print("Belo nome feminino!")
else:
    print("Seu nome é normal")

print("Sergio")