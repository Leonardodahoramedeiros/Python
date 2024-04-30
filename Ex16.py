import math
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateo adjacente: "))

hip = math.hypot(ca, co)

print("O valor da hipotenuza é {:.2f}".format(hip))