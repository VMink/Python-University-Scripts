def armonica(n):
    suma = 1
    contador = 2
    while contador <= n:
        suma += 1 / contador
        contador += 1
    return suma

def main():
    n = float(input("Ingrese un numero: "))
    sumaArmonica = armonica(n)
    print(sumaArmonica)

main()