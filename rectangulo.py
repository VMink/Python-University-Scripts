def rectangulo(ancho,alto):
    for x in range(alto):
        print("+"*ancho) 
    

def main():
    ancho = int(input("Ingrese la anchura: "))
    alto  = int(input("Ingrese la altura: "))
    rectangulo(ancho,alto)
    x = list(range(1,12,3))
    print(x)

main()