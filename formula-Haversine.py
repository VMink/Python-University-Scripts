import math

lat1 = float(input("Ingrese su latitud en radianesde origen: "))
lat2 = float(input("Ingrese su latitud en radianesde destino: "))
lon1 = float(input("Ingrese su longitud en radianes de origen: "))
lon2 = float(input("Ingrese su longitud en radianes de destino: "))

detLat = lat2 - lat1
detLon = lon2 - lon1

R = 6371

a = pow(math.sin(detLat / 2), 2) + math.cos(lat1) * math.cos(lat2) * pow(math.sin(detLon / 2), 2)

c = 2 * math.asin(math.sqrt(a))

d = R * c

print("La distancia en kilometros es: ", round(d,2))