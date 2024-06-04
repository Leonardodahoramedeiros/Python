from time import sleep
numero = int(input("Digite um número: [999 para parar]: "))

contador = 0
soma = 0
while numero != 999:
    soma  = soma + numero
    contador += 1
    numero = int(input("Digite um número: [999 para parar]: "))

print("Você digitou {} números e a soma entre eles foi {}.".format(contador, soma))
