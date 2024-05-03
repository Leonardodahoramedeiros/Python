from random import randint

computador = randint(0, 5) #Computador pensa em um número entre 0 e 5 

jogador = int(input("Digite um valor: ")) #Jogador tenta adivinhar

print("-=-"*20)

print("Vou pensar em um número entre 0 e 5, tente adivinhar!")

print("-=-"*20)

if computador == jogador:
    print("Acertou")
else:
    print("O número que pensei foi {} e o que você escolheu é {}".format(computador, jogador))