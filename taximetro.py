distanciaKilometros = float(input("Cual fue la distancia recorrida en kilometros: "))

distanciaMetros = distanciaKilometros * 1000

banderazo = 14.00

taximetro = (distanciaMetros // 100) * 2.25

total = banderazo + taximetro

print("El total a pagar es de: $", total)
