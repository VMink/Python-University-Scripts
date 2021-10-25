""" import math

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

x1 = (-1 * b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
x2 = (-1 * b - math.sqrt(b**2 - 4 * a * c)) / 2 * a

print("Las soluciones de la ecuacion son: ")
print("Raíz positiva:", x1)
print("Raiz negativa:", x2)  """

import math

print("El área y volumen del cilindro")

r = float(input("Introduzca del radio: "))
h = float(input("Introduzca la altura: "))

area = (2*math.pi*r)*(h + r)
volumen = math.pi * (r**2) * h

print("El área del cilindro es:", area)
print("El volumen del cilindro es:", volumen)