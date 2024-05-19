soma = 0
contador = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
       soma = soma + numero
       contador = contador  + 1
   
print("A soma de todos os valores é {} e tiveram {} números adicionados".format(soma, contador))


       
