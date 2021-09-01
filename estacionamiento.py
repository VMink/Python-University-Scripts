def tarifa_estacionamiento(horas,minutos):
    tarifa = 12

    if horas >= 1 and minutos > 1:
        tarifa *= horas

        if 0 <= minutos <= 15:
            return tarifa + 5
        elif 16 <= minutos <= 30:
            return tarifa + 8
        elif 31 <= minutos <= 45:
            return tarifa + 10
        elif 46 <= minutos <= 59:
            return tarifa + 12
    else:
        return tarifa

def main():
    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese los minutos: "))
    tarifa = tarifa_estacionamiento(horas,minutos)
    print("Su total a pagar es:", tarifa)

main()