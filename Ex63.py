from random import randint
contador = 0
cont = 0

print('''Sou seu computador ...
Acabei de penser em um número entre 0 e 10.
Será que você consegue advinhar qual foi? ''')
computador = randint(0, 10)
palpite = int(input("Qual é o seu palpite: "))

while palpite != computador:
    if palpite < computador:
        print("Mais... Tente novamente!")
        palpite = int(input("Qual é o seu palpite: "))
        contador = contador + 1
    if palpite > computador:
        print("Menos... Tente novamente!")
        palpite = int(input("Qual é o seu palpite: "))
        cont = cont + 1
   
total = contador + cont
print("Acertou com {} tentativas. Parabéns".format(total))

