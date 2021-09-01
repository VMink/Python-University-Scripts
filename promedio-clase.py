e1 = int(input("Ingrese la calificacion del examen 1: "))
e2 = int(input("Ingrese la calificacion del examen 2: "))
e3 = int(input("Ingrese la calificacion del examen 3: "))

pf = int(input("Ingresa la calificacion del proyecto final: "))

promedioExamen = ((e1 + e2 + e3) / 3) * 0.70

pf = pf * 0.30

calificacionFinal = promedioExamen + pf

if calificacionFinal < 70:
    print("REPROBADO CON: ", calificacionFinal)
elif calificacionFinal >= 70:
    print("APROBADO CON: ", calificacionFinal)