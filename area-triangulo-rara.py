import math

a = float(input("Ingrese el lado a de su triangulo: "))
b = float(input("Ingrese el lado b de su triangulo: "))
c = float(input("Ingrese el lado c de su triangulo: "))

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("El area de su triangulo es: ", round(area, 2))