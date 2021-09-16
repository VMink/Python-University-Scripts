def multiplos(inicio, fin, n):
    for x in range(inicio, (fin+1)):
        if x % n == 0:
            print(x)

def main():
    inicio = int(input("Ingrese el inicio: "))
    fin = int(input("Ingrese el fin: "))
    n = int(input("Ingrese el multiplo: "))
    multiplos(inicio, fin, n)

main()