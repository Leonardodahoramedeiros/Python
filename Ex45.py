nota = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota + nota_2) / 2

if(media >= 6):
    print("Tirando {} e {} sua média é {}".format(nota, nota_2, media))
    print("O aluno está Aprovado")

elif(media >= 4 and media < 6):
    print("Tirando {} e {} sua média é {}".format(nota, nota_2, media))
    print("O aluno está em RECUPERAÇÃO")
else:
    print("Tirando {} e {} sua média é {}".format(nota, nota_2, media))
    print("VocÊ foi reprovado direto")
