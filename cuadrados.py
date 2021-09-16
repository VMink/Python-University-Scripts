def cuadrados(n):
    if n >= 1:
        for x in range(n, 0, -1):
            print(pow(x,2))
    else:
        print("Ingrese un numero valido")

def main():
    n = int(input("Ingrese un numero: "))
    cuadrados(n)

main()