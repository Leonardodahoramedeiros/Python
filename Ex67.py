print("Gerado de PA")
print("=-"*20)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
termo = primeiro

contador = 1 
total = 0
mais = 10 

while mais != 0:
    total = total + mais 
    while contador <= total:
        print("{} -> ".format(termo), end=' ')
        termo += razao
        contador+=1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar mais? "))

print("Progressão finalizada com {} termos mostrador".format(total))
