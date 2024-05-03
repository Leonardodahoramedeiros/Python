Velocidade = int(input("Digite a velocidade autal do carro: "))

if Velocidade <= 80:
    print("Tenha um bom dia dirija com segurança")
else:
    multa = (Velocidade - 80) * 7
    print("Você foi multado, pois estava acima da velocidade!")
    print("O valor da sua multa é R${},00".format(multa))