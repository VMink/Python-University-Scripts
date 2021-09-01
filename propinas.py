total = float(input("Ingrese el total de la cuenta: "))

comensales = int(input("Ingrese la cantidad de comensales: "))

print("B: Bueno \nR: Regular\nM: Mala")
servicio = str(input("Ingrese la calidad del servicio: "))

propina = .10

if comensales > 4:
    propina = .15

if (servicio.upper() == 'B') or (servicio.upper() == 'M') or (servicio.upper() == 'R'):
    if servicio.upper() == 'B':
        propina += .02
    elif servicio.upper() == 'M':
        propina -= .02

    pagoFinal = total + (total * propina)

    print("Su total a pagar es: ", pagoFinal)

else:
    print("ERROR por favor elija un valor valido para la calidad del servicio")