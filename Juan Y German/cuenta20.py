def cuenta20():
    positivo = 0
    negativo = 0
    cero = 0
    contador = 0
    while(contador < 20):
        numero = float(input("Ingrese un numero: "))
        if numero == 0:
            cero += 1
        elif numero < 0:
            negativo += 1
        else:
            positivo += 1
        contador += 1
    print("Numeros positivos:", positivo)
    print("Numeros negativos:", negativo)
    print("Numeros de ceros:", cero)

cuenta20()