def en_orden(lista):
    sortedLista = []
    for x in lista:
        sortedLista.append(x)
    sortedLista.sort()
    if lista == sortedLista:
        return True
    else:
        return False


def main():
    print(f'en_orden([10, 17, 24, 30, 40, 55, 70, 85]) = {en_orden([10, 17, 24, 30, 40, 55, 70, 85])}')
    print(f'en_orden([91, 24, 13, 45, 41, 38, 27, 23, 96, 79]) = {en_orden([91, 24, 13, 45, 41, 38, 27, 23, 96, 79])}')
    print(f'en_orden([10, 17, 24, 30, 40, 55, 70, 85, 5]) = {en_orden([10, 17, 24, 30, 40, 55, 70, 85, 5])}')
    print(f'en_orden([11, 10, 17, 24, 30, 40, 55, 70, 85]) = {en_orden([11, 10, 17, 24, 30, 40, 55, 70, 85])}')

main()