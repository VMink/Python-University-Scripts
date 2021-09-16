def rectangulo(ancho,alto,cantidad):
    for x in range(ancho):
        print("* ", end="")
    print()

    for x in range(cantidad):
        for y in range(alto - 2):
            print("* ", end="")
            for z in range(ancho - 2):
                print("  ", end="")
            print("*")
        for y in range(ancho):
            print("* ", end="")
        print()

def main():
    ancho = int(input("Ingrese la anchura: "))
    alto  = int(input("Ingrese la altura: "))
    cantidad = int(input("Ingrese la cantidad de rectangulos: "))
    rectangulo(ancho,alto,cantidad)

main()