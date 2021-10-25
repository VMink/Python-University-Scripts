def comparar_matrices(m1,m2):
    return len(m1) == len(m2) and len(m1[0]) == len(m2[0])

def crea_matriz(tam_ren, tam_col):
    """
    Función que crea y regresa una matriz de tamaño tam_ren X tam_col
    inicializada con 0s. Observa que los subíndices de la matriz son
    valores que van de 0  a tam-1.
    """
    matriz = []
    for ren in range(tam_ren):
        matriz.append([0] * tam_col)
    return matriz

def muestra_matriz(mat):
    """
    Función que muestra en la pantalla los datos de la matriz mat.
    """
    for ren in range(len(mat)):
        for col in range(len(mat[0])):
            print(f'{mat[ren][col]:5}', end='')
        print()

def multiplicar_escalar(m, n):
    matriz = []
    for i in range(len(m)):
        matriz.append([])
        for j in range(len(m[0])):
            valor = m[i][j] * n
            matriz[i].append(valor)
    return matriz

def sumar_matrices(m1, m2):
    matriz = []
    if comparar_matrices(m1,m2) is True:
        for renglon in range(len(m1)):
            lista_columnas = []
            for columna in range(len(m1[0])):
                resultado_suma = m1[renglon][columna] + m2[renglon][columna]
                lista_columnas.append(resultado_suma)
            matriz.append(lista_columnas)
        return matriz
    else:
        print("Las matrices no son del mismo tamaño")

def multiplicar_matrices(m1, m2):
    if len(m1[0]) == len(m2) or len(m1) == len(m2[0]):
        matriz = crea_matriz(len(m1),len(m2[0]))
        for i, ren in enumerate(m1):
            for j, col in enumerate(m2[i]):
                for k, col2 in enumerate(m1[i]):
                    matriz[i][j] += m1[i][k] * m2[k][j]
        return matriz
    else:
        print("Las matrices no son del mismo tamaño")

def es_identidad(m):
    '''Función que recibe una matriz y regrese True si m es una matriz identidad o False en caso contrario'''
    if len(m[0]) == len(m):
        for i,ren in enumerate(m):
            for j,col in enumerate(ren):
                if i == j:
                    if m[i][j] != 1:
                        return False
                elif m[i][j] != 0:
                    return False
    else:
        return False
    return True

def main():
    m1 = [[2, 3, 5], [1, 2, 4], [0, 9, 2]]
    m2 = [[4, 6, 10], [2, 4, 8], [0, 18, 4]]
    m3 = [[1, 2, 3], [4, 5, 6]]
    m4 = [[7, 8], [9, 10], [11, 12]]
    m5 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    m6 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

    print('Probando multiplicar_escalar')
    print(f'{m1} * {2} =')
    muestra_matriz(multiplicar_escalar(m1, 2))
    print()

    print(f'{m2} * {3} =')
    muestra_matriz(multiplicar_escalar(m2, 3))
    print()

    print('Probando sumar_matrices')
    print(f'{m1} + {m2} =')
    muestra_matriz(sumar_matrices(m1, m2))
    print()
    print(f'{m1} + {m5} =')
    muestra_matriz(sumar_matrices(m1, m5))
    print()
    print(f'{m1} + {m3} =')
    sumar_matrices(m1, m3)
    print()
    
    print('Probando multiplicar_matrices')
    print(f'{m1} + {m2} =')
    muestra_matriz(multiplicar_matrices(m1, m2))
    print()
    print(f'{m3} + {m4} =')
    muestra_matriz(multiplicar_matrices(m3, m4))
    print()
    
    print('Probando es_identidad')
    print(f'{m1} es identidad?')
    print(es_identidad(m1))
    print()
    print(f'{m5} es identidad?')
    print(es_identidad(m5))
    print()
    print(f'{m6} es identidad?')
    print(es_identidad(m6))
    print()

main()