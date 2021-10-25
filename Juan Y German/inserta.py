def inserta(lista,elem,pos):
    lst = []
    for x in range(len(lista)):
        if x == pos:
            lst.append(elem)
            lst.append(lista[x])
        else:
            lst.append(lista[x])
    return lst

def main():
    lista = [0,1,2,4,5]
    elem = 'Aqui'
    pos = 3
    insertaResultado = inserta(lista,elem,pos)
    print(insertaResultado)

main()