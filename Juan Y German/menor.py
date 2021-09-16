conjunto = [10,5,5,1,3,6,5,8,2,1,0]

def menor(numDatos):
    menor = conjunto[0]
    for x in numDatos:
        if x < menor:
            menor = x
    return menor

def main():
    datoMenor = menor(conjunto)
    print(datoMenor)

main()