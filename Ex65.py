numero = int(input('''Digite um número para
calcular seu fatorial: '''))

print("Calculando {}!".format(numero), end = ' ')

mult = 1

for i in range(numero, 0, -1):
    mult = mult * i
    if i > 0:
        print(i, end = '')
    if i > 1:
        print(end = ' x ')
print(" = {}".format(mult))
    


