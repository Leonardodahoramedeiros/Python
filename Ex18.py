import random

a = input("Digite o nome do primeiro aluno: ")
b = input("Digite o nome do segundo aluno: ")
c = input("Digite o nome do terceiro aluno: ")
d = input("Digite o nome do quarto aluno: ")

list = (a, b, c, d)

aleatorio = random.choice(list)

print("O aluno escolhido foi {}!".format(aleatorio))