def rectangulo(ancho,alto,cantidad):
    contador = 0
    while contador < cantidad:
        for x in range(ancho):
            print("*", end="")
        print("")

        for x in range(alto - 2):
            print("*", end="")
            for y in range(ancho - 2):
                print(" ", end="")
            print("*")

        for x in range(ancho):
            print("*", end="")
        print("")
        print("")
        print("")
        contador += 1

def main():
    ancho = int(input("Ingrese la anchura: "))
    alto  = int(input("Ingrese la altura: "))
    cantidad = int(input("Ingrese la cantidad de rectangulos: "))
    rectangulo(ancho,alto,cantidad)

main()