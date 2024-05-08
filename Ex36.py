salario = int(input("Digite seu salário: "))

if salario <= 1250:
    aumento = salario * 1.15
    print("Seu novo salario é de R${}".format(aumento))
else:
    aumento = salario * 1.10
    print("Seu novo salario é de R${}".format(aumento))