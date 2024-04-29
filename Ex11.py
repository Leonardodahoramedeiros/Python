Largura = float(input("Digite a largura da parede: "))
Altura = float(input("Digite a altura da parede: "))

Area = Largura * Altura
Tinta = Area / 2 

print("Sua parede tem a dimensão de {}x{} e sua área é {}m²!".format(Largura, Altura, Area))
print("Para pintar essa parede , você precisará de {}L  de tinta!".format(Tinta))

