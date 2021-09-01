import math

ve = float(input("Ingrese la velocidad efectiva del propulsor: "))
m0 = float(input("Ingrese la masa inicial del objeto: "))
mf = float(input("Ingrese la masa final del objeto: "))

detV = ve * math.log(m0 / mf)

print("El cambio de velocidad del objeto es: ", detV)
