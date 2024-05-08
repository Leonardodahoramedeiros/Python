from datetime import date
ano = int(input("Digite o ano em que nasceu: "))

ano_atual = date.today().year
idade = ano_atual - ano

print("Quem nasceu em {} tem {} anos em {}".format(ano, idade, ano_atual))

if idade < 18:
    alistamento = 18 - idade
    ano_alistamento = ano + idade + alistamento
    print("Ainda faltam {} para seu alistamento!".format(alistamento))
    print("Seu alistamento será em {}".format(ano_alistamento))
elif idade == 18:
    print("Está no ano de se alistar")
    print("Seu alistamento será em {}".format(ano_atual))
    

