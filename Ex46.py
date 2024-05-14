from datetime import date
atual = date.today().year

nascimento = int(input("Digite sua idade: "))
idade = atual - nascimento 

print("O atleta tem {}".format(idade))
if(idade <= 9):
    print("Sua categoria é MIRIM")
elif(idade > 9 and idade <= 14):
    print("Sua categoria é INFANTIL")
elif(idade > 14 and idade <= 19):
    print("Sua categoria é Junior")
elif(idade > 19 and idade <= 25):
    print("Sua categoria é Senior")
else:
    print("Você é da categoria Master")