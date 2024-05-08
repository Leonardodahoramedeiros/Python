Km = int(input("Digite a distancia da viagem: "))

if Km <= 200:
    valor = Km * 0.50
    print("O valor da viagem é R${},00".format(valor))
else:
    valor = Km * 0.45
    print("O valor da sua viagme é {}".format(valor))