numero = float(input("Ingrese un numero: "))

if numero % 2 == 0 and numero > 0:
    print("Su numero es par positivo")
elif numero % 2 != 0 and numero > 0:
    print("Su nuemero es impar positivo")
elif numero == 0:
    print("Su numero es 0")
elif numero % 2 == 0 and numero < 0:
    print("Su numero es par negativo")
elif numero % 2 != 0 and numero < 0:
    print("Su numero es impar negativo")