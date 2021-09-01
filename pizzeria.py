def costo_pizza(tamaño, numIngredientes):
    if tamaño.upper() == 'I':
        return individual(numIngredientes)
    elif tamaño.upper() == 'M':
        return mediana(numIngredientes)
    elif tamaño.upper() == 'F':
        return familiar(numIngredientes)
    else:
        return -1
 
def individual(numIngredientes):
    if numIngredientes == 1:
        return 80
    elif numIngredientes == 2:
        return 110
    elif numIngredientes == 3 or numIngredientes == 4:
        return 135
    else:
        return -1

def mediana(numIngredientes):
    if numIngredientes == 1:
        return 100
    elif numIngredientes == 2:
        return 130
    elif numIngredientes == 3 or numIngredientes == 4:
        return 155
    else:
        return -1

def familiar(numIngredientes):
    if numIngredientes == 1:
        return 140
    elif numIngredientes == 2:
        return 170
    elif numIngredientes == 3 or numIngredientes == 4:
        return 195
    else:
        return -1

def main():
    tamaño = str(input("Ingrese el tamaño de la pizza: "))
    numIngredientes = int(input("Ingrese el numero de ingredientes: "))
    print(costo_pizza(tamaño, numIngredientes))

main()