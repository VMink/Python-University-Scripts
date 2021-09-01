A = float(input("Ingrese un numero: "))
B = float(input("Ingrese otro numero: "))
C = float(input("Un ultimo y ya: "))

if A + B == C:
    print("Su tercer numero es la suma de los primeros 2")
elif A + C == B:
    print("Su segundo numero es la suma del primero y el ultimo")
elif C + B == A:
    print("Su primer numero es la suma de los ultimos 2")
else:
    print("Ningun numero es la suma de los otros")