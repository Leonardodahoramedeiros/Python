numero = int(input("Digite um número: "))
razao = int(input("Digite a razao: "))

for i in range(numero, 11, razao):
    print("{}".format(i), end = ' -> ')
print("ACABOU")
