print("="*20)

print("ANALISANDO UM TRIANGULO")

print("="*20)

a = float(input("Primeiro segmento: "))
b = float(input("Segundo sgmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Esses valores podem formar um trinangulo!")
else:
    print("Esses valores não podem formar um triangulo!")


