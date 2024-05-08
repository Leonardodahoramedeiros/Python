print("="*30)
print("Cardapio")

print("1 - Pastel")
print("2 - X - Salada")

print("="*30)

produto = int(input("Digite o numero do produto: "))
quantidade = int(input("Digite a quantidade: "))

if produto == 1:
    produto = 4.50
    nome = 'Pastel'
    conta = produto * quantidade
    print("O produto escolhido foi {} e o valor da sua comanda deu R${}".format(nome, conta))
else:
    produto = 7.50
    nome = "X-SALADA"
    conta = produto * quantidade
    print("O produto escolhido foi {} e o valor da sua comanda deu R${}".format(nome, conta))
    

