def tabla(numero):
    for x in range(0,10):
        print(numero,"x",x,"=",numero*x)

def main():
    numero = int(input("Ingrese un numero: "))
    tabla(numero)

main()