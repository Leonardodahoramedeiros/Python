import math

angulo = float(input("Digite o angulo que deseja: "))

seno = math.sin(math.radians(angulo))
print("O seno desse angulo é {:.2f}".format(math.sin(seno)))
cos = math.cos(math.radians(angulo))
print("O cosseno desse angulo é {:.2f}".format(math.cos(cos)))
tan = math.tan(math.radians(angulo))
print("A tangente desse angulo é {:.2f}".format(math.tan(tan)))