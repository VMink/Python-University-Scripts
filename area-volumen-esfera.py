import math

radio = float(input("Ingrese el radio de su esfera: "))

area = 4 * math.pi * pow(radio, 2)

volumen = (4 * math.pi * pow(radio, 3)) / 3

print("El area de su esfera es: ", round(area, 2))
print("El volumen de su esfera es: ", round(volumen, 2))