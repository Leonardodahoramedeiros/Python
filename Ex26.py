Nome = str(input("Digite seu primeiro nome: ")).strip()

n = Nome.split()

print("Muito prazer em te conhcer! ")

print("Seu primeiro nome é {}".format(n[0]))
print("Seu sobrenome é {}".format(n[len(n)-1]))
