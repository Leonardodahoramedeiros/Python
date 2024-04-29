dias = int(input("Quantos dias alugado: "))
km = int(input("Quantos Km rodados: "))

valor = (dias*60) + (km*0.15)



print("O valor total a pagar é R${}".format(valor))