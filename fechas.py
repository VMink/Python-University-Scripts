def siguiente_dia(dia,mes,año):
    maxDia = 31
    maxMes = 12

    if dia > 31 or mes > 12:
        return "Error"

    if mes == 2:
        maxDia = 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        maxDia = 30
    
    dia += 1

    if dia > maxDia:
        dia = 1
        mes += 1

    if mes > maxMes:
        mes = 1
        año += 1

    return dia, mes, año

def main():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    print("El día siguiente es:", siguiente_dia(dia,mes,año))

main()