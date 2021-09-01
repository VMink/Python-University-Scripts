articulos = int(input("De cuantos articulos es el pedido? "))

tarifa = 109.50

extra = (articulos - 1) * 29.50

envio = tarifa + extra

print("El total a pagar es de $", envio)