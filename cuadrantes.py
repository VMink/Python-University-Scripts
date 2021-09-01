def cuadrante(x,y):
    if x == 0 and y == 0:
        print("Se encuentra en el origen")
    elif (x > 0 and y >= 0) or (x >= 0 and y > 0):
        print("Se encuentra en el primer cuadrante")
    elif (x < 0 and y >= 0) or (x <= 0 and y > 0):
        print("Se encuentra en el segundo cuadrante")    
    elif (x < 0 and y <= 0) or (x <= 0 and y < 0):
        print("Se encuentra en el tercer cuadrante")
    elif (x > 0 and y <= 0) or (x >= 0 and y < 0):
        print("Se encuentra en el cuarto cuadrante")

def main():
    x = float(input("Ingrese la coordenada x: "))
    y = float(input("Ingrese la coordenada y: "))
    cuadrante(x,y)

main()