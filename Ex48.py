print("=" *20, " LOJAS LEONARDO ", "=" *20)

compra = float(input("Digite o valor da compra: "))

print('''FORMAR DE PAGAMENTO
    [ 1 ] A dinheiro ou cheque
    [ 2 ] A vista no cartão 
    [ 3 ] 2x no cartão 
    [ 4 ] 3 x ou mais no cartão''')

opcao = int(input("Digite a opção: "))

if opcao == 1:
    valor = compra * 0.85
    print("Sua compra de R${},00 vai ficar R${},00 ".format(compra, valor))
elif opcao == 2:
    valor = compra * 0.90
    print("Sua compra de R${},00 vai ficar R${},00".format(valor, compra))
elif opcao == 3:
    print("O valor da sua compra ficará R${},00".format(compra))
else:
    vezes = int(input("Digite a quantidade de vezes: "))
    if vezes < 3:
        print("Erro!")
    else:
        valor = compra * 1.20
        parcela = valor / 10
        print('''Sua compra parcelada em {}x de R${} com juros
        Sua compra de R${} vai custar R${} no final'''.format(vezes, parcela, compra, valor ))
