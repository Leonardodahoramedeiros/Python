soma_idade = 0
maior = 0
menor = 0
contador = 0
contagem = 0
for i in range(1, 5):
    print("=" * 5, "{}º".format(i), "=" * 5)
    Nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Sexo: [M/F]: "))
    soma_idade = soma_idade + idade
    if idade > maior and sexo == 'M':
        maior = idade
        estilo = "homem"
        N = Nome
    else:
        if idade > 20:
            contador = contador + 1
        else:
            contagem = contagem + 1
            sx = 'mulher'

media = soma_idade / i

print("A media das idades é {}".format(media))
print("O homem {} mais velho tem {} e seu Nome é {}".format(estilo, maior, N))
print("Ao todo são {} {} com  menos de 20 anos ".format(contagem, sx))
