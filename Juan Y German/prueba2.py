def estadisticosInventario(inv):
    sumaProductos = 0
    sumaCostos = 0
    acumuladorCostos = 0
    for i in inv:
        sumaProductos += i[2]
        sumaCostos += i[3]
        acumuladorCostos += 1
    costoPromedio = sumaCostos / acumuladorCostos

    print(sumaProductos)
    print(costoPromedio)

estadisticosInventario([[13,"Do",5,20],[74,"Mi",15,30],[18,"La",20,25],[27,"Mi",20,5]])