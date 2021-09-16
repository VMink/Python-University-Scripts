def rectangulo(ancho,alto):
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

def main():
    ancho = int(input("Ingrese la anchura: "))
    alto  = int(input("Ingrese la altura: "))
    rectangulo(ancho,alto)

main()