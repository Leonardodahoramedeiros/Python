valor_1 = int(input("Digite o primeiro valor: "))
valor_2 = int(input("Digite o segundo valor: "))
valor_3 = int(input("Digite o terceiro valor: "))

list = [valor_1, valor_2, valor_3]
maior = max(list)
menor = min(list)
print("A menor nota digita é {}".format(menor))
print("O maior valor é {}".format(maior))