def nones(lista):
    nones = []
    for x in lista:
        if x % 2 != 0:
            nones.append(x)
    return nones

def main():
    lista = [0,3,4,-5,6,7,56789,-987]
    nonesLista = nones(lista)
    print(nonesLista)

main()