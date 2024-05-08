Casa =  float(input("Digite o valor da casa: "))
salario = int(input("Digite o salario do comprador: "))
Tempo = float(input("Digite a quantidade de ano: "))

meses = Tempo *12
Parcela = Casa / meses

if Parcela >= salario * 0.30:
    print("Para pagar uma casa do valor R${} em {} anos a prestação será de R${:.2f}".format(Casa, Tempo, Parcela))
    print("Empréstimo negado!")
else:
    print("Para pagar uma casa do valor R${} em {} anos a prestação será de R${:.2f}".format(Casa, Tempo, Parcela))
    print("Empréstimo Concedido!")
