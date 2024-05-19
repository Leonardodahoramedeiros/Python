from datetime import date

soma = 0
add = 0
data = date.today().year

for i in range(1, 8):
    idade = int (input("Digite a idade da {}º pessoa: ".format(i)))
    conta = data - idade 
    if conta < 18:
        soma = soma + 1
        
    else:
        add = add + 1
        
print("Temos {} pessoas mais novas".format(soma))
print("Temos {} pessoas mais velhas".format(add))