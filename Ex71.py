valor = int(input("Quer ver a tabuada de qual valor: "))

print("=-"*20)

contador = 0

while valor > 0:

    for i in range(1, 11):
        print("{} x {} = {}".format(i, valor, i * valor))
        contador = contador + 1

    valor = int(input("Quer ver a tabuada de qual valor: "))
    
print("=-"*20)
print("PROGRAMA DE TABUADA ENCERRADO! VOLTE SEMPRE!")