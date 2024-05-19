Numero = int(input("Digite um número: "))
contador = 0
for i in range(1, Numero + 1):
    if Numero % i == 0:
        contador = contador + 1
        print('\033[m',i, end = ' ')
    else:
        print('\033[34m',i, end = ' ')

print("\nO número {} foi divido {} vezes!".format(Numero, contador))
if contador == 2:
    print("Número Primo")
else:
    print("Não é primo")