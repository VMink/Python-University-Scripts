A = int(input("Ingrese un numero: "))
B = int(input("Ingrese otro numero: "))
C = int(input("Un ultimo y ya: "))

if A <= B and A >= C:
    print(A, "Es su numero intermedio")
elif A >= B and A <= C:
    print(A, "Es su numero intermedio")
elif B <= A and B >= C:
    print(B, "Es su numero intermedio")
elif B >= A and B <= C:
    print(B, "Es su numero intermedio")
elif C <= A and C >= B:
    print(C, "Es su numero intermedio")
elif C >= A and C <= B:
    print(C, "Es su numero intermedio")