Numero = int(input("Digite um número: "))

u = Numero // 1 % 10 
d = Numero // 10 % 10
c = Numero // 100 % 10
m = Numero // 1000 % 10

print("Analisando o formato do número {}".format(Numero))
print(" {} Unidades!".format(u))
print(" {} dezenas!".format(d))
print(" {} centenas!".format(c))
print(" {} milhar!".format(m))

