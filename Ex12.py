Produto = float(input("Digite o valor do produto: "))
Desconto = Produto * 0.95

print("O produto custava R${},00 e com o desconto de 5%, passou a custar R${:.2f},00".format(Produto, Desconto))