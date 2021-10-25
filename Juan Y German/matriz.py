def crea_matriz(ren,col,val):
    matriz = []
    for x in range(ren):
        matriz.append([x+val] * col)
    return matriz

def main():
    ren = 4
    col = 5
    val = 1
    matriz = crea_matriz(ren,col,val)
    print(matriz)

main()