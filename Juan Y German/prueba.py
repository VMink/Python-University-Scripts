def calculo_membresia(lista, x):
    membresia = 0
    a = lista[0]
    b = lista[1]
    c = lista[2]
    d = lista[3]

    if x < a or x > d:
        return membresia
    elif (a <= x and x <= b):
        operacion = float((x - a) / (b - a))
        membresia = float(operacion)
    elif (b <= x and x <= c):
        membresia = 1
    elif(c <= x and x <= d):
        operacion = float((d - x) / (d - c))
        membresia = float(operacion)

    return membresia

def main():
    txt = open('./funciones.txt')
    
    listaParametros = []
    for i in txt:
        i = i[:-1]
        split = i.split(',')
        intTransforms = []
        for j in split:
            intTransforms.append(int(j))
        listaParametros.append(intTransforms)
    
    for i in listaParametros:
        lista = []
        lista.append(i[0])
        lista.append(i[1])
        lista.append(i[2])
        lista.append(i[3])
        x = i[4]
        print(calculo_membresia(lista,x))


main()
