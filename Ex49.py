from random import randint
from time import sleep

print('''Suas opções
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA  ''')
itens = ('Pedra', 'Papel', "Tesoura")
computador = randint(0,2)
jogador = int(input("Qual é a sua jogada: "))

print("="*25)
print("O computador jogou {} ".format(itens[computador]))
print("O jogador jogou {}".format(itens[jogador]))
print("="*25)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)
if jogador == 0:
    if computador == 0:
        print("Empate!")
    elif computador == 1:
        print("Computador ganhou:")
    elif computador == 2:
        print("Computador ganhou")
    else:
        print("Invalido")
elif jogador == 1:
    if computador == 0:
        print("Computador perdeu!")
    elif computador == 1:
        print("Empate")
    elif computador == 2:
        print("Computador ganhou")
    else:
        print("Inválido")
elif jogador == 2:
    if computador == 0:
        print("Computador perdeu")
    elif computador == 1:
        print("Computador perdeu")
    elif computador == 2:
        print("Empate")
    else:
        print("Inválido")
