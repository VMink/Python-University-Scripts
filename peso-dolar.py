pesos = float(input("Ingrese su cantidad en pesos: "))
dolares = 22.5

conversion = pesos // dolares #Aqui uso division entera
                              #para que no regrese centavos

print("Su total es: ", conversion, " dolares")