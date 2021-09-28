# Define aqui tus funciones
def inserta(lista,elem,pos):
    lst = []
    for x in range(len(lista)):
        if x == pos:
            lst.append(elem)
            lst.append(lista[x])
        else:
            lst.append(lista[x])
    return lst
            

def cuenta_letra(palabra, letra):
    lst = []
    for i in palabra:
        lst.append(i)
    return lst.count(letra)
        
def cuenta_letra_palabras(palabras, letra):
    num_letras = 0
    for palabra in palabras:
        num_letras += cuenta_letra(palabra,letra)
    return num_letras

def cuenta_letras_palabras(palabras,letras):
    lst = []
    for letra in letras:
        valor = cuenta_letra_palabras(palabras,letra)
        lst.append(valor)
    return lst

def fibonacci(i):
    a = 0
    b = 1
    lst = []
    if i > 2:
        lst.append(a)
        for x in range(i-1):
            lst.append(b)
            b = a + b
            a = b - a
    else:
        lst.append(a)
        lst.append(b)
    return lst

# No modifiques el codigo despues de esta linea
def main():
    # Probando inserta
    print(f'inserta([0, 1, 2, 3], 4, 0) = {inserta([0, 1, 2, 3], 4, 0)}')
    print(f'inserta(["a", "c", "e"], "b", 2) = {inserta(["a", "c", "e"], "b", 2)}')
    print(f'inserta([20, 10, 40, 22], 100, 3) = {inserta([20, 10, 40, 22], 100, 3)}')
    
    palabras = ['palabras', 'de', 'pruuuuueba', 'mas', 'paaalaaabraaas']
    letras = ['a', 'c', 'p', 'u', 'b', 'e']
    
    # Probando cuenta_letra
    for palabra in palabras:
        for letra in letras:
            print(f'cuenta_letra(\'{palabra}\', \'{letra}\') = {cuenta_letra(palabra, letra)}')
    
    # Probando cuenta_letra_palabras
    for letra in letras:
        print(f'cuenta_letra_palabras({palabras}, \'{letra}\') = {cuenta_letra_palabras(palabras, letra)}')
    
    # Probando cuenta_letras_palabras
    print(f'cuenta_letras_palabras({palabras}, {letras}) = {cuenta_letras_palabras(palabras, letras)}')
    
    # Probando fibonacci
    for i in range(8):
        print(f'fibonacci({i}) = {fibonacci(i)}')

main()
    