peso = int(input("Digite seu peso: "))
altura = float(input("Digite seu peso: "))

IMC = peso / (altura ** 2)

print("O IMC dessa pessoa é {:.2f}".format(IMC))

if(IMC < 25):
    print("Peso Ideal")
elif(IMC >= 25 or IMC < 30):
    print("Sobrepeso")
elif(IMC >= 30 or IMC < 40):
    print("Obesidade")
else:
    print("Obesidade Mórbida")