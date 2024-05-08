numero = int(input("Digite um número: "))

print('''Escolha um das bases para conversão:
      [ 1 ] Converter para binário
      [ 2 ] Converter para octal 
      [ 3 ] Converter para Hexadecimal''')
opção = int(input("Digite a opção:"))

if opção == 1:
    print("O valor {} e em binario fica assim {}".format(numero, bin(numero)))
elif opção == 2:
    print("O valor {} e em binario fica assim {}".format(numero, oct(numero)))
elif opção == 3:
    print("O valor {} e em binario fica assim {}".format(numero, hex(numero)))
else:
    print("Opção inválida, tente novamente")


