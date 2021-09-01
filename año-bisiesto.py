def es_bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0 and año % 400 != 0:
            print("No es bisiesto")
            return 
        if año % 400 == 0:
            print("Es bisiesto")
            return
        print("Es bisiesto")
    else:
        print("No es bisiesto")


def main():
    año = int(input("Ingrese un año: "))
    es_bisiesto(año)


main()