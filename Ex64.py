from time import sleep

numero_1 = int(input("Digite o primeiro valor: "))
numero_2 = int(input("Digite o segundo valor: "))
print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
opcao = int(input("Digite sua opcao: "))

while opcao != 5:
    if opcao == 1:
        somar = numero_1 + numero_2
        print("A soma entre {} e {} é {}".format(numero_1, numero_2, somar))
        opcao = int(input("Digite sua opcao: "))
    if opcao == 2:
        mult = numero_1 * numero_2 
        print("A multiplicação entre {} e {} é {}".format(numero_1, numero_2, mult))
        opcao = int(input("Digite sua opcao: "))
    if opcao == 3:
        if numero_1 > numero_2:
            print("Entre {} e {} o valor {} é maior!".format(numero_1, numero_2, numero_1))
            opcao = int(input("Digite sua opcao: "))
        if numero_2 > numero_1:
            print("Entre {} e {} o valor {} é maior!".format(numero_2, numero_1, numero_2))
            opcao = int(input("Digite sua opcao: "))
    if opcao == 4:
        numero_1 = int(input("Digite o primeiro valor: "))
        numero_2 = int(input("Digite o segundo valor: "))
        print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
        opcao = int(input("Digite sua opcao: "))
    if opcao > 5:
        print("Opção inválida. Tente novamente")
        opcao = int(input("Digite sua opcao: "))

print("Finalizando...")
sleep(2)

print("Fim do programa! Volte sempre!")



    


  