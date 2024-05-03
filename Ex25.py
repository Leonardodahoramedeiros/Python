#STRIP serve para não contar se tiver espações

frase = str(input( "Digite a frase: ")).upper().strip()

print("A letra A aparece {}".format(frase.count("A")))
print("A primeira vez que a leta A aparece é na posição {}".format(frase.find("A")+1))
print("A ultima ocorrência de A {} apareceu na posição".format(frase.rfind("A")+1))