########### PROGRAMA 1
def cuenta20():
    contador = 0
    positivos = 0
    negativos = 0
    ceros = 0
    while contador < 20:
        numero = float(input("Ingrese un numero: "))
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1
        contador += 1
    print("Usted ingreso", positivos, "numeros positivos,", negativos, "numeros negativos y", ceros, "ceros")

########### PROGRAMA 2
def cuenta15():
    contador = 0
    while contador < 15:
        numero = float(input("Ingrese un numero NEGATIVO: "))
        print("Su numero POSITIVO es:", numero * -1)
        contador += 1

########### PROGRAMA 3
def tablaMultiplicar(num):
    contador = 0
    multiplicador = 0
    while contador < 11:
        print(num,"x",multiplicador,"=",num*multiplicador)
        multiplicador += 1
        contador += 1

########### PROGRMA 4
def menor(numDatos):
    contador = 0
    datos = []
    while contador < numDatos:
        num = float(input("Ingrese un numero: "))
        datos.append(num)
        contador += 1
    numMenor = datos[0]
    for x in datos:
        if x < numMenor:
            numMenor = x
    print("El numero mayor del conjunto de datos es:",numMenor)

########### PRGROMA 5
def mayor(numDatos):
    contador = 0
    datos = []
    while contador < numDatos:
        num = float(input("Ingrese un numero: "))
        datos.append(num)
        contador += 1
    numMayor = datos[0]
    for x in datos:
        if x > numMayor:
            numMMayor = x
    print("El numero mayor del conjunto de datos es:",numMMayor)

############ PROGRAMA 6
def teatro():
    dineroPerdido = 0
    costoBoleto = 200
    while True:
        edad = int(input("Ingrese la edad: "))
        if 0 < edad < 4:
            print("No entra")
        elif (5 <= edad <= 14) or (edad >= 66):
            descuento = costoBoleto * 0.35
            dineroPerdido += descuento
            print("Su descuento es de:", descuento, "\nSu boleto cuesta:", costoBoleto - descuento)
        elif (15 <= edad <= 19) or (46 <= edad <= 65):
            descuento = costoBoleto * 0.25
            dineroPerdido += descuento
            print("Su descuento es de:", descuento, "\nSu boleto cuesta:", costoBoleto - descuento)
        elif 20 <= edad <= 45:
            descuento = costoBoleto * 0.10
            dineroPerdido += descuento
            print("Su descuento es de:", descuento, "\nSu boleto cuesta:", costoBoleto - descuento)
        elif edad == 0:
            break
    print("Dinero perdido:",dineroPerdido)

############## PROGRAMA 7
def multiplos3o5():
    contador = 0
    acumulador = 0
    while contador < 1000:
        if contador % 3 == 0 or contador % 5 == 0:
            print(contador)
            acumulador += contador
        contador += 1
    print("La suma es:",acumulador)

############## PROGRAMA 8
def primo(num):
    contador = 2
    while contador < num:
        if num % contador == 0:
            return False
        contador += 1
    return True

############## PROGRAMA 9
def primos(num):  
    contador = 2
    acumulador = 0
    while contador < num:
        if primo(contador) == True: ########### AQUI ESTOY REUTILIZANDO LA FUNCION DE ARRIBA, PARA QUE TAMBIEN LA METAN EN ESTE PROGRAMA
            acumulador += 1
        contador += 1
    print("Hay", acumulador, "números primos")

############### GERMAN YA TIENE EL PROGRAMA 10

############### PROGRAMA 11
def sumaFibonacci():
    a, b = 0,1
    suma = 0
    while a < 4000000:
        suma += a
        a, b = b, a+b
    print("La suma de la sucesion de fibonacci para 4 millones es:", suma)

primos(23)