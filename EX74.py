numero = int(input("Digite um valor: "))

soma = 0

for i in range(1, numero + 1):
    soma = soma + i
    print("{} + {} = {}".format(i, i, soma))

print(soma)
