soma = 0
for i in range(1, 7):
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0:
        soma = soma + numero

print("A soma dos valores é {}".format(soma))